# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Render expects $PORT, default 10000)
EXPOSE 10000

# Start with gunicorn (assuming app.py defines "app")
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]