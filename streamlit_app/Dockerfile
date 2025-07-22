# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# Create a requirements.txt if you don't have one, e.g.:
# streamlit
# pymongo
# pandas
# plotly
RUN pip install --no-cache-dir streamlit==1.35.0 pymongo pandas plotly

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the Streamlit app when the container launches
# --server.port 8501: ensures Streamlit runs on the exposed port
# --server.address 0.0.0.0: makes the app accessible from outside the container
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]