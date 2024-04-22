import logging
from apps.baselayer.baseapiviews import BaseAPIView
from django.conf import settings

from apps.clients.openweathermap import OpenWeatherMapClient

logger = logging.getLogger(settings.LOGGER_NAME_PREFIX + __name__)


class WeatherAPIView(BaseAPIView):

    def get(self, request, *args, **kwargs):
        try:
            city = kwargs.get("city")
            client = OpenWeatherMapClient()
            data = client.get_weather_by_city(city)
            return self.send_success_response(
                data=data, message="Success", msg_code=0
            )
        except Exception as err:
            logger.exception(err)
            return self.send_bad_request_response(
                msg_code=1, message="Something went wrong!"
            )


class AverageTemperatureAPIView(BaseAPIView):

    def get(self, request, *args, **kwargs):
        try:
            cities = kwargs.get("cities").split(",")
            client = OpenWeatherMapClient()
            avg_temp = client.get_average_temperature_for_cities(cities)
            return self.send_success_response(
                data={
                    "average_temp": avg_temp
                }, message="Success", msg_code=0
            )
        except Exception as err:
            logger.exception(err)
            return self.send_bad_request_response(
                msg_code=1, message="Something went wrong!"
            )
