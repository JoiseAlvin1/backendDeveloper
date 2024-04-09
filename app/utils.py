import requests
from django.conf import settings
api_key = settings.OPENWEATHERMAP_API_KEY


def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def get_average_temperature(city_list):
    temperatures = []
    for city in city_list:
        city = city.replace('%20', '')
        data = get_weather(city)
        if 'main' in data:
            temperature = data['main']['temp']
            temperatures.append(temperature)
    if temperatures:
        average_temperature = sum(temperatures) / len(temperatures)
        average_temperature = round(average_temperature-273.15, 2)
        return average_temperature
    return None