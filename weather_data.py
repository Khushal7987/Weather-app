import requests
import json
from datetime import datetime

# --- CONFIGURATION (REPLACE THESE) ---
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Get this from a free weather API service
CITY = "London"
# -------------------------------------

def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Simple dictionary to hold the request parameters
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use Celsius
    }
    
    print(f"Fetching weather for {city}...")
    
    try:
        # 1. Make the API request (the simple code for the 'tough' network task)
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        # 2. Get the JSON data
        data = response.json()
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_and_display(data, city):
    """Parses the complex JSON data using standard Python dictionary access."""
    if not data:
        print("No data available.")
        return

    # Standard Python dictionary access for parsing
    main_weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    sunrise_ts = data['sys']['sunrise']
    sunset_ts = data['sys']['sunset']

    # Convert Unix timestamps to human-readable time
    sunrise = datetime.fromtimestamp(sunrise_ts).strftime('%H:%M:%S')
    sunset = datetime.fromtimestamp(sunset_ts).strftime('%H:%M:%S')

    # --- Simple Output Formatting ---
    print("\n" + "="*40)
    print(f"Weather Report for {city.upper()}")
    print("="*40)
    print(f"🌡️ Temperature: {temp}°C")
    print(f"☁️ Condition:   {main_weather} ({description.title()})")
    print(f"💧 Humidity:    {humidity}%")
    print(f"💨 Wind Speed:  {wind_speed} m/s")
    print(f"🌅 Sunrise:     {sunrise}")
    print(f"🌇 Sunset:      {sunset}")
    print("="*40)

# --- EXECUTION ---
weather_data = get_weather_data(CITY, API_KEY)
if weather_data:
    parse_and_display(weather_data, CITY)
