# Dockerfile for Language-Identification-Application-Backend

# Use an official Python runtime as a parent image
FROM python:3.9-slim AS backend-builder

# Set the working directory in the container
WORKDIR /app

# Install required Python packages
RUN pip install Flask Flask-CORS scikit-learn

# Copy the application code to the working directory
COPY . .

# Expose port 5000 (default Flask port)
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]


