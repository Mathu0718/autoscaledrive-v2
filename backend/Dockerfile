# Base image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy files
COPY . .

# Install Flask
RUN pip install flask

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
