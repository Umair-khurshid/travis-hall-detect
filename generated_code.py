import requests

def get_weather_data(city):
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?q={city}')
    temp = current_temperature  
    return temp
