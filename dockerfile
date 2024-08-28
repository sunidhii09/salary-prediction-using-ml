# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the backend code into the container at /app
COPY backend /app/backend

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Define environment variable
ENV PYTHONPATH=/app/backend

# Run the FastAPI server
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
