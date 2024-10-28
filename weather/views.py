import os
import requests
from django.http import HttpResponse

OPENWEATHER_API_KEY = '2259844c882b2649f6a638e2f8a25ade'
OPENWEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    
    if not lat or not lon:
        return HttpResponse("Latitude and Longitude are required parameters", status=400)

    weather_data = fetch_weather_data(lat, lon)

    return HttpResponse(weather_data, content_type="application/json")

def fetch_weather_data(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric" 
    }
    
    response = requests.get(OPENWEATHER_API_URL, params=params)
    response.raise_for_status()
    return response.json()
