# data_reader/data_reader/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_reader.settings')

app = Celery('data_reader') # type: ignore

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch-seismic-data-every-60-seconds': {
        'task': 'waveform.tasks.fetch_seismic_data',  
        'schedule': 10.0, 
    },
    'fetch-weather-data-every-60-seconds': {
        'task': 'weather.tasks.fetch_weather_data_task',
        'schedule': 10.0,  
        'args': (35, 139), 
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
