FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./waveform/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ../ ./

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
