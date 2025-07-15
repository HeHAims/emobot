# Use official Python image
FROM python:3.10-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy all code
COPY . .

# Expose Streamlit default port
EXPOSE 7860

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_emobot.py", "--server.port", "7860", "--server.address", "0.0.0.0"]
