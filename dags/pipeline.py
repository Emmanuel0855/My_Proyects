from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import requests
import pymongo
import logging
import re
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# --- Configuration ---
# Use environment variables for MongoDB host and port, falling back to defaults
# These will be set by docker-compose
MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB_NAME = "ETLProjectDB" # A more descriptive DB name

# Alpha Vantage API Key (IMPORTANT: Replace with your actual key if using Alpha Vantage)
# You need to register for a FREE API key at https://www.alphavantage.co/support/#api-key
ALPHA_VANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
STOCK_SYMBOLS = ["IBM", "MSFT", "GOOGL", "AMZN", "AAPL"] # 5 different stock symbols for comparison

# NHTSA vPIC API Base URL (Open Source, No Key Required)
NHTSA_VPIC_BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"

# --- MongoDB Utilities ---
def get_mongodb_client():
    """Establishes and returns a MongoDB client connection."""
    try:
        client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        logger.info(f"Successfully connected to MongoDB at {MONGO_HOST}:{MONGO_PORT}")
        return client
    except pymongo.errors.ConnectionFailure as e:
        logger.error(f"Could not connect to MongoDB: {e}")
        raise # Re-raise the exception to fail the task if connection fails

# --- API Helper ---
def extract_api_data(url: str) -> dict:
    """Fetches JSON data from a given URL."""
    logger.info(f"Attempting to extract data from: {url}")
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        logger.info(f"Successfully extracted data from: {url}")
        return resp.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during API extraction from {url}: {e}")
        return {} # Return empty dict on error

# --- Ingestion Tasks ---
def ingest_currency(**kwargs):
    """Ingests currency exchange rate data into MongoDB."""
    ti = kwargs['ti']
    # ExchangeRate-API (Open Source, No Key Required)
    raw_data = extract_api_data("https://api.exchangerate-api.com/v4/latest/USD")
    if not raw_data:
        logger.warning("No currency data extracted. Skipping ingestion.")
        ti.xcom_push(key='currency_raw_count', value=0)
        return

    client = get_mongodb_client()
    db = client[MONGO_DB_NAME]
    collection = db["raw_currency"]
    # Clear previous raw data to keep only the latest batch, ensuring idempotency
    collection.delete_many({})
    collection.insert_one(raw_data)
    client.close()
    num_rates = len(raw_data.get('rates', {}))
    logger.info(f"[Ingest] Ingested currency data. Rates for USD: {num_rates} currencies.")
    ti.xcom_push(key='currency_raw_count', value=num_rates)

def ingest_stocks(**kwargs):
    """Ingests daily stock data for specified symbols into MongoDB."""
    ti = kwargs['ti']
    client = get_mongodb_client()
    db = client[MONGO_DB_NAME]
    collection = db["raw_stocks"]
    # Clear previous raw data to keep only the latest batch for all symbols, ensuring idempotency
    collection.delete_many({})
    
    total_ingested_stocks = 0
    for symbol in STOCK_SYMBOLS:
        # Alpha Vantage API (Requires a FREE API Key)
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
        raw_data = extract_api_data(url)
        
        if raw_data and "Time Series (Daily)" in raw_data:
            # Add symbol and timestamp to raw data for better tracking
            raw_data['symbol'] = symbol
            raw_data['ingestion_timestamp'] = datetime.utcnow().isoformat()
            collection.insert_one(raw_data)
            total_ingested_stocks += 1
            logger.info(f"[Ingest] Ingested daily stock data for {symbol}.")
        else:
            logger.warning(f"[Ingest] Failed to ingest stock data for {symbol}. Response: {raw_data}")
    
    client.close()
    logger.info(f"[Ingest] Total stock symbols ingested: {total_ingested_stocks}")
    ti.xcom_push(key='stocks_raw_count', value=total_ingested_stocks)

def ingest_car_makes(**kwargs):
    """Ingests car makes data from NHTSA vPIC API into MongoDB."""
    ti = kwargs['ti']
    # NHTSA vPIC API (Open Source, No Key Required)
    url = f"{NHTSA_VPIC_BASE_URL}/GetMakesForVehicleType/car?format=json"
    raw_data = extract_api_data(url)
    if not raw_data or not raw_data.get('Results'):
        logger.warning("No car makes data extracted. Skipping ingestion.")
        ti.xcom_push(key='car_makes_raw_count', value=0)
        return

    client = get_mongodb_client()
    db = client[MONGO_DB_NAME]
    collection = db["raw_car_makes"]
    collection.delete_many({}) # Ensure idempotency
    collection.insert_one({"timestamp": datetime.utcnow().isoformat(), "data": raw_data['Results']})
    client.close()
    num_makes = len(raw_data['Results'])
    logger.info(f"[Ingest] Ingested {num_makes} car makes.")
    ti.xcom_push(key='car_makes_raw_count', value=num_makes)

def ingest_car_models(**kwargs):
    """Ingests car models data for specific make IDs from NHTSA vPIC API into MongoDB."""
    ti = kwargs['ti']
    # Pull selected make IDs from XCom, which were pushed by 'transform_car_makes'
    selected_make_ids = ti.xcom_pull(task_ids='transform_car_makes', key='selected_make_ids')
    
    if not selected_make_ids:
        logger.warning("No make IDs found via XCom for car models ingestion. Skipping.")
        ti.xcom_push(key='car_models_raw_count', value=0)
        return

    client = get_mongodb_client()
    db = client[MONGO_DB_NAME]
    collection = db["raw_car_models"]
    collection.delete_many({}) # Clear previous raw data for idempotency

    total_models_ingested = 0
    for make_id in selected_make_ids:
        url = f"{NHTSA_VPIC_BASE_URL}/GetModelsForMakeId/{make_id}?format=json"
        raw_data = extract_api_data(url)
        if raw_data and raw_data.get('Results'):
            doc = {
                "make_id": make_id,
                "timestamp": datetime.utcnow().isoformat(),
                "data": raw_data['Results'] # Store models as a list under 'data'
            }
            collection.insert_one(doc)
            total_models_ingested += len(raw_data['Results'])
            logger.info(f"[Ingest] Ingested {len(raw_data['Results'])} models for Make ID {make_id}.")
        else:
            logger.warning(f"No models found for Make ID {make_id} or API error. Response: {raw_data}")
    
    client.close()
    logger.info(f"[Ingest] Total car models ingested: {total_models_ingested}.")
    ti.xcom_push(key='car_models_raw_count', value=total_models_ingested)

# --- Transformation Functions ---
def process_currency_data(raw_data: dict) -> dict:
    """Processes raw currency data for standardization and enrichment."""
    processed = {
        "base_currency": raw_data.get("base"),
        "last_update_utc": datetime.fromtimestamp(raw_data.get("time_last_updated", 0)).isoformat(), # ISO 8601
        "exchange_rates": {}
    }
    rates = raw_data.get("rates", {})
    # Enrichment: specific common rates and a count of available rates
    processed["exchange_rates"]["USD_to_EUR"] = rates.get("EUR")
    processed["exchange_rates"]["USD_to_GBP"] = rates.get("GBP")
    processed["exchange_rates"]["USD_to_JPY"] = rates.get("JPY")
    processed["exchange_rates"]["USD_to_MXN"] = rates.get("MXN")
    processed["total_available_rates"] = len(rates)
    return processed

def process_stock_data(raw: dict) -> list:
    """Processes raw stock data for standardization, cleaning, and enrichment."""
    processed_records = []
    symbol = raw.get('symbol')
    time_series = raw.get("Time Series (Daily)", {})

    if not symbol or not time_series:
        logger.warning(f"Invalid raw stock data for processing: {raw.keys()}")
        return []

    for date_str, values in time_series.items():
        try:
            # Standardization: snake_case, ISO 8601 for date
            record = {
                "symbol": symbol,
                "date": datetime.strptime(date_str, "%Y-%m-%d").isoformat(),
                "open_price": float(values.get("1. open", 0)),
                "high_price": float(values.get("2. high", 0)),
                "low_price": float(values.get("3. low", 0)),
                "close_price": float(values.get("4. close", 0)),
                "volume": int(values.get("5. volume", 0)),
            }
            # Cleaning: Remove records with critical missing fields (e.g., if close_price is 0 unexpectedly)
            if record["close_price"] == 0 and record["open_price"] == 0:
                logger.warning(f"Skipping record for {symbol} on {date_str} due to zero prices.")
                continue

            # Enrichment: daily_change, daily_range, is_volatile_day
            record["daily_change"] = record["close_price"] - record["open_price"]
            record["daily_range"] = record["high_price"] - record["low_price"]
            # Example flag: is_volatile_day if range is more than 2% of open price
            record["is_volatile_day"] = bool(record["open_price"] and record["daily_range"] / record["open_price"] > 0.02)
            
            processed_records.append(record)
        except (ValueError, TypeError) as e:
            logger.warning(f"Error processing stock record for {symbol} on {date_str}: {e}. Data: {values}")
    return processed_records

def process_car_makes_data(**kwargs):
    """Processes raw car makes data for standardization and enrichment, and pushes selected make IDs to XCom."""
    ti = kwargs['ti']
    client = get_mongodb_client()
    db = client[MONGO_DB_NAME]
    # Fetch the latest raw car makes document
    raw_data_doc = db["raw_car_makes"].find_one(sort=[('_id', pymongo.DESCENDING)])
    
    if not raw_data_doc or not raw_data_doc.get('data'):
        logger.warning("No raw car makes data found for processing.")
        ti.xcom_push(key='processed_car_makes_count', value=0)
        ti.xcom_push(key='selected_make_ids', value=[]) # Push empty list if no data
        client.close()
        return

    processed_makes = []
    for item in raw_data_doc['data']:
        try:
            processed = {
                "make_id": int(item.get("Make_ID")),
                "make_name": item.get("Make_Name"),
                "vehicle_type": item.get("VehicleTypeName"),
                "processing_timestamp_utc": datetime.utcnow().isoformat()
            }
            # Cleaning: remove records with missing critical fields
            if not processed["make_id"] or not processed["make_name"]:
                logger.warning(f"Skipping car make due to missing ID or name: {item}")
                continue
            
            # Enrichment: Example - flag for common makes (simple classification)
            common_makes = ["FORD", "CHEVROLET", "TOYOTA", "HONDA", "BMW", "MERCEDES-BENZ", "AUDI", "NISSAN", "HYUNDAI", "KIA", "VOLKSWAGEN"]
            processed["is_common_make"] = processed["make_name"].upper() in [m.upper() for m in common_makes]

            processed_makes.append(processed)
        except (ValueError, TypeError) as e:
            logger.warning(f"Error processing car make record {item}: {e}")

    db["processed_car_makes"].delete_many({}) # Clear previous processed data for idempotency
    if processed_makes:
        db["processed_car_makes"].insert_many(processed_makes)
    
    logger.info(f"[Transform/Load] Processed and loaded {len(processed_makes)} car makes.")
    ti.xcom_push(key='processed_car_makes_count', value=len(processed_makes))

    # XCom: Select top N make IDs to fetch models for
    # Filter for common makes and take their IDs, or just take the first few available
    make_ids_to_fetch_models = []
    for make in processed_makes:
        if make["is_common_make"] and make["make_id"] not in make_ids_to_fetch_models:
            make_ids_to_fetch_models.append(make["make_id"])
        if len(make_ids_to_fetch_models) >= 5: # Limit to 5 for demonstration to avoid too many API calls
            break
    
    # Fallback: If no common makes found or less than 5, take the first few available
    if len(make_ids_to_fetch_models) < 5 and processed_makes:
        for make in processed_makes:
            if make["make_id"] not in make_ids_to_fetch_models:
                make_ids_to_fetch_models.append(make["make_id"])
            if len(make_ids_to_fetch_models) >= 5:
                break

    ti.xcom_push(key='selected_make_ids', value=make_ids_to_fetch_models)
    client.close()


def process_car_models_data(**kwargs):
    """Processes raw car models data for standardization and enrichment."""
    ti = kwargs['ti']
    client = get_mongodb_client()
    db = client[MONGO_DB_NAME]
    
    # Fetch all raw car models documents (each document contains models for a specific make_id)
    raw_models_cursor = db["raw_car_models"].find({})
    
    processed_models = []
    for raw_data_doc in raw_models_cursor:
        make_id = raw_data_doc.get("make_id")
        if not make_id:
            logger.warning(f"Skipping raw car models document due to missing make_id: {raw_data_doc.keys()}")
            continue

        for item in raw_data_doc.get('data', []): # Iterate through the 'data' list within each raw document
            try:
                processed = {
                    "make_id": make_id, # Link back to the make
                    "model_id": int(item.get("Model_ID")), # NHTSA API uses Model_ID
                    "model_name": item.get("Model_Name"), # NHTSA API uses Model_Name
                    "processing_timestamp_utc": datetime.utcnow().isoformat()
                }
                # Cleaning: remove records with missing critical fields
                if not processed["model_id"] or not processed["model_name"]:
                    logger.warning(f"Skipping car model due to missing ID or name: {item}")
                    continue
                
                # Enrichment: Example - add a flag if model name contains numbers
                processed["has_numbers_in_name"] = bool(re.search(r'\d', processed["model_name"]))

                processed_models.append(processed)
            except (ValueError, TypeError) as e:
                logger.warning(f"Error processing car model record {item}: {e}")

    db["processed_car_models"].delete_many({}) # Clear previous processed data for idempotency
    if processed_models:
        db["processed_car_models"].insert_many(processed_models)
    
    logger.info(f"[Transform/Load] Processed and loaded {len(processed_models)} car models.")
    ti.xcom_push(key='processed_car_models_count', value=len(processed_models))
    client.close()

# --- Combined Transformation Task for Currency and Stocks ---
def transform_currency_stocks_data(**kwargs):
    """Processes raw currency and stock data and loads into processed collections."""
    ti = kwargs['ti']
    client = get_mongodb_client()
    db = client[MONGO_DB_NAME]

    # Process Currency
    raw_currency_data = db["raw_currency"].find_one(sort=[('_id', pymongo.DESCENDING)])
    if raw_currency_data:
        processed_currency = process_currency_data(raw_currency_data)
        db["processed_currency"].delete_many({}) # Idempotency
        db["processed_currency"].insert_one(processed_currency)
        logger.info("[Transform/Load] Processed and loaded currency data.")
    else:
        logger.warning("No raw currency data found for processing in transform_currency_stocks_data.")

    # Process Stocks
    raw_stock_data_cursor = db["raw_stocks"].find({})
    total_processed_stocks = 0
    db["processed_stocks"].delete_many({}) # Idempotency
    for raw_stock_doc in raw_stock_data_cursor:
        processed_stocks_for_symbol = process_stock_data(raw_stock_doc)
        if processed_stocks_for_symbol:
            db["processed_stocks"].insert_many(processed_stocks_for_symbol)
            total_processed_stocks += len(processed_stocks_for_symbol)
    logger.info(f"[Transform/Load] Processed and loaded {total_processed_stocks} stock records.")
    client.close()


# --- DAG Definition ---
with DAG(
    dag_id="etl_data_pipeline",
    start_date=days_ago(1),
    schedule_interval=timedelta(days=1), # Run daily
    catchup=False, # Do not run for past missed schedules
    tags=["etl", "data_pipeline", "university_project"],
    doc_md="""
    ### ETL Data Pipeline DAG
    This DAG orchestrates the ingestion, transformation, and loading of data from multiple public APIs
    into MongoDB. It includes:
    - Ingestion of currency exchange rates from ExchangeRate-API (Open Source, No Key).
    - Ingestion of daily stock market data from Alpha Vantage (Requires Free API Key).
    - Ingestion of car makes and models data from NHTSA vPIC API (Open Source, No Key).
    - Dedicated transformation tasks for each dataset, ensuring data quality and enrichment.
    - Utilizes XComs to pass selected Make IDs between tasks for dynamic processing of car models.
    The pipeline is designed to be idempotent, clearing previous data before ingesting/processing new batches.
    """
) as dag:
    # 1. Ingestion Tasks (run in parallel)
    ingest_currency_task = PythonOperator(
        task_id="ingest_currency_data",
        python_callable=ingest_currency,
        provide_context=True, # Required to use XComs
    )

    ingest_stocks_task = PythonOperator(
        task_id="ingest_stock_data",
        python_callable=ingest_stocks,
        provide_context=True,
    )

    ingest_car_makes_task = PythonOperator(
        task_id="ingest_car_makes_data",
        python_callable=ingest_car_makes,
        provide_context=True,
    )

    # 2. Transformation Tasks
    # Transform currency and stocks (depends on their respective ingestion tasks)
    transform_currency_stocks_task = PythonOperator(
        task_id="transform_currency_stocks",
        python_callable=transform_currency_stocks_data,
        provide_context=True,
    )

    # Transform car makes and push selected make IDs to XCom (depends on car makes ingestion)
    transform_car_makes_task = PythonOperator(
        task_id="transform_car_makes",
        python_callable=process_car_makes_data,
        provide_context=True,
    )

    # Ingest car models (depends on transform_car_makes for make IDs via XCom)
    ingest_car_models_task = PythonOperator(
        task_id="ingest_car_models_data",
        python_callable=ingest_car_models,
        provide_context=True,
    )

    # Transform car models data (depends on car models ingestion)
    transform_car_models_task = PythonOperator(
        task_id="transform_car_models",
        python_callable=process_car_models_data,
        provide_context=True,
    )

    # Define task dependencies
    # Ingestion tasks run in parallel
    # Transformation tasks depend on their respective ingestion tasks
    # Car models ingestion depends on car makes transformation (for XCom data)
    # Final car models transformation depends on its ingestion
    ingest_currency_task >> transform_currency_stocks_task
    ingest_stocks_task >> transform_currency_stocks_task

    ingest_car_makes_task >> transform_car_makes_task
    transform_car_makes_task >> ingest_car_models_task
    ingest_car_models_task >> transform_car_models_task