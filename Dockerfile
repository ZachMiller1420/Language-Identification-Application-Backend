# Dockerfile for Language-Identification-Application-Backend

# Use an official Python runtime as a parent image
FROM python:3.9-slim AS backend-builder

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY Language-Identification-Application-Backend/requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application code to the working directory
COPY Language-Identification-Application-Backend/ ./

# Expose port 5000 (default Flask port)
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
