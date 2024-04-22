import requests
from django.conf import settings


class OpenWeatherMapClient:
    def __init__(self):
        self.api_key = settings.OPEN_WEATHER_MAP_ACCESS_KEY
        self.base_url = settings.OPEN_WEATHER_MAP_BASEURL

    def get_weather_by_city(self, city_name):
        weather_data = self._get_weather_data(city_name)
        return weather_data

    def _get_geo_data(self, city_name):
        url = f"{self.base_url}/geo/1.0/direct?q={city_name}&appid={self.api_key}&limit=1"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data:
                return data
            else:
                print("City not found.")
                return None
        except requests.RequestException as e:
            print("Error during geocoding request:", e)
            return None

    def _get_weather_data(self, city_name):
        url = f"{self.base_url}/weather?q={city_name}&APPID={self.api_key}&limit=1"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print("Error during weather request:", e)
            return None

    def get_weather_for_cities(self, city_names):
        weather_data_list = []
        for city_name in city_names:
            weather_data = self.get_weather_by_city(city_name)
            if weather_data:
                weather_data_list.append(weather_data)
        return weather_data_list

    def get_average_temperature_for_cities(client, cities):
        data = client.get_weather_for_cities(cities)
        temperatures = [city_data['main']['temp'] for city_data in data if city_data]
        if temperatures:
            average_temperature = sum(temperatures) / len(temperatures)
            return average_temperature
        else:
            return None
