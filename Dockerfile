# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app/ ./app/

# Expose the port your app runs on (matching your main.py)
EXPOSE 4999

# Set the command to run your Flask app
CMD ["python", "app/main.py"]