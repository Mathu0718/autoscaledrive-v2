# Base image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy files
COPY . .

# ✅ Install Flask and flask_cors
RUN pip install flask flask_cors

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
