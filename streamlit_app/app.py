import streamlit as st

# ✅ Debe ser la primera llamada de Streamlit
st.set_page_config(layout="wide", page_title="ETL Data Dashboard", page_icon="📊")

import pymongo
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# --- Configuration ---
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "ETLProjectDB")

# --- MongoDB Connection ---
@st.cache_resource
def get_mongodb_client():
    try:
        client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        client.admin.command('ismaster')
        st.success(f"Successfully connected to MongoDB at {MONGO_HOST}:{MONGO_PORT}")
        return client
    except pymongo.errors.ConnectionFailure as e:
        st.error(f"Could not connect to MongoDB: {e}")
        st.stop()

client = get_mongodb_client()
db = client[MONGO_DB_NAME]

# --- Data Fetching Functions ---
@st.cache_data(ttl=600)
def fetch_currency_data():
    try:
        data = db.processed_currency.find_one(sort=[('_id', pymongo.DESCENDING)])
        return data if data else {}
    except Exception as e:
        st.error(f"Error fetching currency data: {e}")
        return {}

@st.cache_data(ttl=600)
def fetch_stock_data():
    try:
        data = list(db.processed_stocks.find({}))
        return pd.DataFrame(data) if data else pd.DataFrame()
    except Exception as e:
        st.error(f"Error fetching stock data: {e}")
        return pd.DataFrame()

@st.cache_data(ttl=600)
def fetch_car_makes_data():
    try:
        data = list(db.processed_car_makes.find({}))
        return pd.DataFrame(data) if data else pd.DataFrame()
    except Exception as e:
        st.error(f"Error fetching car makes data: {e}")
        return pd.DataFrame()

@st.cache_data(ttl=600)
def fetch_car_models_data():
    try:
        data = list(db.processed_car_models.find({}))
        flat_models = []
        for doc in data:
            make_id = doc.get('make_id')
            if 'data' in doc and isinstance(doc['data'], list):
                for model_item in doc['data']:
                    model_item['make_id'] = make_id
                    flat_models.append(model_item)
            else:
                flat_models.append(doc)
        return pd.DataFrame(flat_models) if flat_models else pd.DataFrame()
    except Exception as e:
        st.error(f"Error fetching car models data: {e}")
        return pd.DataFrame()

# --- Streamlit App ---
st.title("ETL Data Dashboard")
st.markdown("Insights from Currency Exchange, Stock Markets, and Car Models.")

# --- Sidebar Filters ---
st.sidebar.header("Dashboard Filters")
st.sidebar.markdown("Use the filters below to refine the data displayed in the charts.")

# --- Currency Section ---
st.header("Currency Exchange Rates (USD Base)")
currency_data = fetch_currency_data()

if currency_data:
    st.write(f"Last Updated (UTC): {currency_data.get('last_update_utc', 'N/A')}")
    rates = currency_data.get("exchange_rates", {})
    if rates:
        currency_df = pd.DataFrame(rates.items(), columns=["Currency Pair", "Rate"])
        st.dataframe(currency_df, use_container_width=True, hide_index=True)
        fig_currency = px.bar(
            currency_df,
            x="Currency Pair",
            y="Rate",
            title="USD Exchange Rates (Selected Currencies)",
            labels={"Currency Pair": "Target Currency (vs. USD)", "Rate": "Exchange Rate"},
            color="Rate",
            color_continuous_scale=px.colors.sequential.Viridis
        )
        fig_currency.update_layout(xaxis_title="Currency Pair", yaxis_title="Exchange Rate")
        st.plotly_chart(fig_currency, use_container_width=True)
    else:
        st.info("No exchange rates available in the processed data.")
else:
    st.info("No currency data available. Please ensure the Airflow DAG has run successfully.")

st.markdown("---")

# --- Stock Market Section ---
st.header("Stock Market Performance")
stock_df = fetch_stock_data()

if not stock_df.empty:
    stock_df["date"] = pd.to_datetime(stock_df["date"])
    unique_symbols = sorted(stock_df["symbol"].unique().tolist())
    selected_symbols = st.sidebar.multiselect(
        "Select Stock Symbols",
        options=unique_symbols,
        default=unique_symbols[:min(len(unique_symbols), 3)]
    )
    filtered_stock_df = stock_df[stock_df["symbol"].isin(selected_symbols)]

    if not filtered_stock_df.empty:
        filtered_stock_df = filtered_stock_df.sort_values(by="date")
        fig_close = px.line(
            filtered_stock_df,
            x="date",
            y="close_price",
            color="symbol",
            title="Stock Close Price Over Time",
            labels={"date": "Date", "close_price": "Close Price", "symbol": "Stock Symbol"},
            hover_data={"open_price": True, "high_price": True, "low_price": True, "volume": True, "daily_change": True, "is_volatile_day": True}
        )
        fig_close.update_layout(xaxis_title="Date", yaxis_title="Close Price (USD)")
        st.plotly_chart(fig_close, use_container_width=True)

        fig_daily_change = px.bar(
            filtered_stock_df,
            x="date",
            y="daily_change",
            color="symbol",
            title="Daily Price Change",
            labels={"date": "Date", "daily_change": "Daily Change (USD)", "symbol": "Stock Symbol"},
            barmode="group"
        )
        fig_daily_change.update_layout(xaxis_title="Date", yaxis_title="Daily Change (Close - Open)")
        st.plotly_chart(fig_daily_change, use_container_width=True)
    else:
        st.info("No stock data available for the selected symbols.")
else:
    st.info("No stock data available.")

st.markdown("---")

# --- Car Models Section ---
st.header("Car Makes and Models (from NHTSA vPIC API)")
st.info("Note: This API provides vehicle make and model information, but does not include pricing.")

car_makes_df = fetch_car_makes_data()
car_models_df = fetch_car_models_data()

if not car_makes_df.empty:
    st.subheader("Available Car Makes")
    st.dataframe(car_makes_df[["make_id", "make_name", "vehicle_type", "is_common_make"]].sort_values(by="make_name"), use_container_width=True, hide_index=True)

    unique_makes = sorted(car_makes_df["make_name"].unique().tolist())
    selected_make_name = st.sidebar.selectbox(
        "Select Car Make to view Models",
        options=["All Makes"] + unique_makes,
        index=0
    )

    model_search_query = st.sidebar.text_input("Search Specific Model Name (e.g., 'Accord', 'Civic')").strip().lower()

    if not car_models_df.empty:
        st.subheader("Car Models")
        filtered_models_df = car_models_df.copy()

        if selected_make_name != "All Makes":
            selected_make_id_row = car_makes_df[car_makes_df["make_name"] == selected_make_name]
            if not selected_make_id_row.empty:
                selected_make_id = selected_make_id_row["make_id"].iloc[0]
                filtered_models_df = filtered_models_df[filtered_models_df["make_id"] == selected_make_id]
                st.write(f"Displaying models for **{selected_make_name}**:")
            else:
                st.info("Selected make not found.")
                filtered_models_df = pd.DataFrame()

        if model_search_query and not filtered_models_df.empty:
            filtered_models_df = filtered_models_df[
                filtered_models_df["model_name"].str.lower().str.contains(model_search_query, na=False)
            ]

        st.write(f"Found {len(filtered_models_df)} matching models.")

        if not filtered_models_df.empty:
            st.dataframe(filtered_models_df[["make_id", "model_name", "has_numbers_in_name"]].sort_values(by="model_name"), use_container_width=True, hide_index=True)

            models_per_make_count = filtered_models_df.groupby("make_id").size().reset_index(name="model_count")
            models_per_make_count = pd.merge(models_per_make_count, car_makes_df[["make_id", "make_name"]], on="make_id", how="left")
            models_per_make_count = models_per_make_count.sort_values(by="model_count", ascending=False).head(15)

            if not models_per_make_count.empty:
                fig_models_per_make = px.bar(
                    models_per_make_count,
                    x="make_name",
                    y="model_count",
                    title="Number of Models per Brand (Filtered)",
                    labels={"make_name": "Brand", "model_count": "Number of Models"},
                    color="model_count",
                    color_continuous_scale=px.colors.sequential.Plasma
                )
                fig_models_per_make.update_layout(xaxis_title="Brand", yaxis_title="Number of Models")
                st.plotly_chart(fig_models_per_make, use_container_width=True)
            else:
                st.info("No models found for visualization.")
        else:
            st.info("No models match your filters.")
    else:
        st.info("No car models data available.")
else:
    st.info("No car makes data available.")

st.markdown("---")
st.caption("Data fetched from public APIs and processed via Apache Airflow. Dashboard built with Streamlit.")