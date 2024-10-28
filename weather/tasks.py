import os
from celery import shared_task # type: ignore
from .views import fetch_weather_data

OPENWEATHER_API_KEY = '2259844c882b2649f6a638e2f8a25ade'

@shared_task
def fetch_weather_data_task(lat, lon):
    print(f"Fetching weather data for lat: {lat}, lon: {lon}...")
    
    try:
        weather_data = fetch_weather_data(lat, lon)
        print("Weather data fetched successfully")
        
        output_dir = './tmp_weather/'
        os.makedirs(output_dir, exist_ok=True)
        
        # Write data to file
        output_file = os.path.join(output_dir, 'weather_data.json')
        with open(output_file, 'w') as f:
            f.write(weather_data)
        
        print(f"Weather data written to file at {output_file}")
    
    except Exception as e:
        print(f"Failed to fetch weather data: {e}")
