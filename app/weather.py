import requests
from config import WEATHER_API_KEY
#import logging



def get_weather(city="České Budějovice",
                api_key=None) -> str:
    """
    This function fetches the current weather of a city from the `OpenWeather API`.

    Args:
        city (str): The name of the city for which the weather is to be fetched. (e.g. České Budějovice)
        api_key (str): The API key for the OpenWeather API. If not provided, the value from the environment variable `WEATHER_API_KEY` is used.

    """

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=cz"
        response = requests.get(url)
        response.raise_for_status() # This method calls exception if status code of request is not 200
        
        weather_data = response.json()

        # Extracting data from json as current weather status (cloudy, windy, etc...) and temp in °C 
        weather = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]

        return f"Aktuální počasí: {weather}, teplota: {temp}°C."
        
        
    except requests.exceptions.RequestException as e:
        #logging.error(f"Chyba při získávaní počasí: {e}")
        return "Aktuální počasí je nedostupné."
    
