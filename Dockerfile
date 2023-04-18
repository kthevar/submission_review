# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5002

# Set the environment variables for authentication
ENV USERNAME your_username
ENV PASSWORD your_password

# Start the application
CMD ["python", "app.py"]
