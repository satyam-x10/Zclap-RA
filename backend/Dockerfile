FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS-level dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your backend code
COPY . /app

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
