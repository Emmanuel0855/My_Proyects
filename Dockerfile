# Use the official Airflow base image
FROM apache/airflow:2.8.1-python3.11

# Install necessary Python packages for Airflow and your DAGs
# Ensure that all packages listed in requirements.txt are compatible with Airflow's Python version
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt