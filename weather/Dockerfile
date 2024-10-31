# Dockerfile for weather
FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./weather/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy manage.py from the data_reader directory
COPY manage.py ./

# Copy the weather directory
COPY ./weather ./weather

# Expose the application port
EXPOSE 8001

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
