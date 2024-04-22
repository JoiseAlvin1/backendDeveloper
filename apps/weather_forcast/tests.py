from django.test import TestCase

class WeatherAPITestCase(TestCase):

    def test_weather_endpoint_success(self):
        response = self.client.get('/weather/london')
        self.assertEqual(response.status_code, 200)

    def test_weather_endpoint_city_not_found(self):
        response = self.client.get('/weather/nonexistent_city')
        self.assertEqual(response.status_code, 200)

class AverageTemperatureAPITestCase(TestCase):

    def test_average_temperature_endpoint_success(self):
        response = self.client.get('/weather/average-temperature/lahore,peshawar')
        self.assertEqual(response.status_code, 200)

    def test_average_temperature_endpoint_no_cities_provided(self):
        response = self.client.get('/weather/average-temperature/')
        self.assertEqual(response.status_code, 404)


