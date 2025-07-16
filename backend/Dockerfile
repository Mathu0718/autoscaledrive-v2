# Base image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install flask flask-cors boto3

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
