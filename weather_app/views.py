from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TasksSerializer
from decouple import config
import requests

API_KEY = config('OPENWEATHER_API_KEY')  # using the api key stored in .env file
# Create your views here.


class WeatherDataAPIView(APIView):
    """Browsable REST-API for fetching weather data based on a given city"""

    @staticmethod  # static method as no interaction with the self/instance is required
    def get(request, **kwargs):
        """
        Takes a city as a parameter
        Returns weather data
        """

        city = kwargs.get('city')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            return Response(data=weather_data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AverageWeatherDataAPIView(APIView):
    """Browsable REST-API for calculating average temperature for the given cities"""

    @staticmethod  # static method as no interaction with the self/instance is required
    def get(request, **kwargs):
        """
        Takes a list of comma-separated cities as a parameter
        Returns average temperature for the given cities upto 2 decimals
        """

        cities_with_commas = kwargs.get('cities')
        cities_list = cities_with_commas.split(',')  # generating a cities list
        temperature_sum = float()  # declaring a float for the total temperature

        # looping through each city, getting its temperature and adding it to the sum
        for city in cities_list:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
            response = requests.get(url=url)
            if response.status_code == 200:
                weather_data = response.json()

                # calculating sum of temperatures for all the given cities
                temperature_sum += weather_data.get('main',{}).get('temp',0)
            else:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:  # calculating average temperature
            average_temperature = temperature_sum/len(cities_list)
        except ZeroDivisionError:  # raising value error in case of 0 cities
            raise ValueError("No cities were passed")

        return Response(data={"average_temperature": round(average_temperature, 2)})


class TasksViewSet(ModelViewSet):
    """
    Browsable REST-API View for performing operations on Tasks
    ViewSet gives predefined functions for CRUD operations
    """

    queryset = Task.objects.all()  # getting all the tasks to populate view set
    serializer_class = TasksSerializer  # specifying the serializer class

