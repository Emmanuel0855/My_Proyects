🚀 End-to-End Batch ETL Data PipelineOrchestrated with Apache Airflow, MongoDB & Streamlit

✨ Project Overview
This project showcases a robust, end-to-end Batch ETL (Extract, Transform, Load) pipeline. It's designed to ingest data from various public APIs, process it, store it in a MongoDB database, and then present dynamic insights through an interactive Streamlit web dashboard. The entire solution is fully containerized using Docker Compose, ensuring easy setup, portability, and reproducibility across different environments.

🎯 Objective
Our primary goal with this project is to demonstrate a comprehensive data engineering workflow, covering:

Data Ingestion: Extracting data from diverse real-world public APIs.

Data Transformation: Applying standardization, cleaning, and enrichment techniques to raw data.

Data Storage: Efficiently managing both raw and processed datasets in a NoSQL database (MongoDB).

Orchestration: Building complex, scheduled data workflows using Apache Airflow.

Visualization: Delivering interactive data insights via a web-based Streamlit dashboard.

Containerization: Packaging the entire application for seamless deployment using Docker.

🌐 Data Sources & APIsThis pipeline integrates data from the following external services:

💰 ExchangeRate-APIPurpose: Provides up-to-date currency exchange rates.Endpoint Example: https://api.exchangerate-api.com/v4/latest/USDRelevance: Offers insights into global currency valuations and economic trends.

📈 Alpha Vantage APIPurpose: Delivers real-time and historical financial market data, including daily stock prices.Endpoint Example: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=YOUR_API_KEYRelevance: Enables analysis of stock performance, volatility, and market trends.

🔑 Requirement: A free API key from Alpha Vantage is necessary. Remember to update dags/main_pipeline.py with your key!

🚗 NHTSA vPIC API (National Highway Traffic Safety Administration - Vehicle Product Information Catalog)Purpose: Provides comprehensive vehicle specifications, including car makes and models.Endpoint Examples:https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/car?format=json (for car manufacturers)https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/{make_id}?format=json (for models by manufacturer ID)Relevance: Offers insights into the automotive industry's diversity.
⚠️ Important Note: This free API does NOT provide car pricing information. Therefore, the Streamlit dashboard will filter by brand and model, but not by price.

🏛️ Infrastructure ArchitectureThe project's services are defined and managed within the docker-compose.yaml file, creating a cohesive environment:mongodbTechnology: MongoDB (NoSQL Database)Port: 27017Role: The primary data sink for both raw and processed data from the ETL pipeline.postgresTechnology: PostgreSQL (Relational Database)Role: Dedicated metadata store for Apache Airflow (DAG states, task history, logs). Crucially, this database is NOT used for storing the ingested pipeline data.webserver (Airflow)Technology: Apache AirflowPort: 8080Role: Provides the user interface for managing, scheduling, and monitoring your DAGs.scheduler (Airflow)Technology: Apache AirflowRole: Monitors all defined DAGs and triggers tasks based on their schedules and dependencies.streamlitTechnology: Streamlit (Web Application Framework)Port: 8501Role: Hosts the interactive web dashboard that connects to MongoDB to visualize the processed data.All services communicate securely within a dedicated Docker network named my_airflow_network.

📁 Project Structureyour-project-name/
├── dags/
│   └── main_pipeline.py  # 🐍 Airflow DAG definition and core ETL logic
├── streamlit_app/
│   ├── app.py            # 📊 Streamlit dashboard application code
│   ├── Dockerfile        # 🐳 Dockerfile for building the Streamlit image
│   └── requirements.txt  # 📦 Python dependencies for the Streamlit app
├── docker-compose.yaml   # 🐳 Defines all Docker services and their configurations
├── Dockerfile            # 🐳 Dockerfile for building Airflow components (webserver, scheduler)
├── requirements.txt      # 📦 Python dependencies for Airflow services (e.g., requests, pymongo, pandas)
├── mongo_data/           # 💾 Persistent volume for MongoDB data
└── postgres_data/        # 💾 Persistent volume for PostgreSQL data


⚙️ Setup & Running the ProjectFollow these steps to deploy and run the ETL pipeline and dashboard on your local machine:PrerequisitesDocker Desktop (or Docker Engine and Docker Compose) installed and running.1. Initial Project SetupEnsure your local project directory mirrors the Project Structure outlined above.Place the provided main_pipeline.py into dags/.Place app.py, Dockerfile, and requirements.txt into streamlit_app/.The docker-compose.yaml and your Airflow Dockerfile should be in the root of your project.2. Configure Alpha Vantage API KeyObtain your free API key from Alpha Vantage.Open dags/main_pipeline.py and replace the placeholder YOUR_ALPHA_VANTAGE_API_KEY with your actual key.3. Initialize Airflow Database & Create UserThis crucial step sets up Airflow's internal database and creates an admin user for the UI.Stop all existing Docker Compose services (if any are running from previous attempts):docker-compose down
Start only PostgreSQL and MongoDB (Airflow's dependencies):docker-compose up -d postgres mongodb
Allow a few seconds for these databases to fully initialize.Initialize the Airflow database:docker-compose run --rm webserver airflow db init
This command will set up the necessary tables in the PostgreSQL database.Create an Airflow admin user:docker-compose run --rm webserver airflow users create \
    --username admin \
    --firstname Airflow \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password password

Feel free to change admin, Airflow, User, admin@example.com, and password to your desired credentials.4. Build & Run All Docker ContainersAfter the database is initialized and the user is created, you can launch all services:docker-compose up -d --build
docker-compose up -d --build: This command builds (or rebuilds if changes are detected) and starts all services in detached mode (in the background).Initial startup may take several minutes as images are downloaded and built. You can monitor progress with docker ps.🚀 Airflow DAG: etl_data_pipelineThe etl_data_pipeline DAG, defined in dags/main_pipeline.py, orchestrates the entire ETL process.DAG Structure & TasksThe DAG is structured into 7 interconnected tasks:Ingestion Tasks (Parallel):ingest_currency_data: Fetches the latest USD exchange rates.ingest_stocks_data: Fetches daily time series stock data for predefined symbols.ingest_car_makes_data: Fetches a list of car manufacturers (makes).These tasks extract raw JSON data and store it directly into respective raw_ collections in MongoDB.Transformation Tasks & Chained Ingestion:transform_currency_stocks: Processes raw currency and stock data (standardization, cleaning, enrichment) and loads it into processed_currency and processed_stocks collections.transform_car_makes: Processes raw car makes data, and importantly, uses Airflow XCom to push a list of selected make_ids (e.g., for popular brands) to the next task.ingest_car_models_data: This task dynamically pulls make_ids from XCom (from transform_car_makes) and fetches car models for those specific makes from the NHTSA vPIC API, storing them in raw_car_models.transform_car_models: Processes the raw car models data and loads it into the processed_car_models collection.Task DependenciesThe flow of data and execution is defined as:graph TD
    A[ingest_currency_data] --> C(transform_currency_stocks)
    B[ingest_stocks_data] --> C
    D[ingest_car_makes_data] --> E(transform_car_makes)
    E --> F[ingest_car_models_data]
    F --> G(transform_car_models)
XCom UsageXComs (Cross-Communication) are strategically used to pass small, critical pieces of information between tasks. For instance, transform_car_makes pushes a filtered list of make_ids, which ingest_car_models_data then retrieves to fetch only relevant car models.How to Trigger & Monitor the DAGAccess Airflow UI: Open your web browser and navigate to http://localhost:8080.Log In: Use the admin credentials you created.Unpause the DAG: On the DAGs page, locate etl_data_pipeline and toggle its switch to "On".Trigger Manually: Click the "Play" button (▶️) next to the DAG name to start a new run.Monitor Progress: Click on the DAG name to view the Graph View or Grid View. Tasks will change color (e.g., green for success, red for failure).Check Logs: For detailed output, click on a specific task instance in the Graph/Grid View, then click "Logs".🗄️ MongoDB IntegrationMongoDB serves as the central data repository:Raw Data: Unprocessed data from APIs is stored in collections like raw_currency, raw_stocks, raw_car_makes, and raw_car_models. This preserves the original API responses.Processed Data: Cleaned, standardized, and enriched data is stored in processed_currency, processed_stocks, processed_car_makes, and processed_car_models collections, optimized for consumption by the dashboard.Connectivity: Both Airflow tasks and the Streamlit app connect to MongoDB using the pymongo library, leveraging Docker's internal networking (mongodb as the hostname).📊 Streamlit DashboardThe Streamlit dashboard (streamlit_app/app.py) provides an interactive web interface for visualizing the processed data.How to Access the DashboardEnsure all Docker services are running (docker-compose up -d).Open your web browser and navigate to http://localhost:8501.Dashboard FeaturesCurrency Exchange Rates: Displays the latest USD exchange rates in both tabular and graphical formats.Stock Market Performance: Visualizes historical close prices and daily changes for selected stock symbols with interactive line and bar charts. You can filter by stock symbol.Car Makes and Models: Presents car makes and models data from the NHTSA vPIC API.Filter by Brand (Make): Select one or more car brands from a multi-select dropdown.Search by Model Name: Use a text input to search for specific car models (e.g., "Civic", "F-150").Note: As the API does not provide pricing, price-based filters are not available in this section.Real-time Insights: The dashboard dynamically fetches the latest processed data from MongoDB, ensuring your visualizations are always up-to-date after each successful Airflow DAG run.✅ Submission Checklist[ ] GitHub repository with all code, configurations, and Dockerfiles.[ ] docker-compose.yml correctly defines all necessary services: Airflow (webserver, scheduler), PostgreSQL, MongoDB, and Streamlit.[ ] Functional etl_data_pipeline DAG in Airflow with at least 5 tasks, demonstrating ingestion, transformation, and XCom usage.[ ] Working Streamlit dashboard accessible on http://localhost:8501, displaying processed data and offering interactive filters for car models (brand, specific model).[ ] Clear, complete, and well-structured README.md (this document).