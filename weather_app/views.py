import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import *
from .serializers import *
import requests

# Create your views here.

class WeatherDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        city = kwargs.get('city')
        api_key = 'd5478237dac7aa890c813beb9e3cc206'
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url=url)
        if response.status_code == 200:
            weather_data = response.json()
            return Response(data=weather_data)
        else:
            return None
class AverageWeatherDataAPIView(APIView):
    def get(self,request,*args, **kwargs):
        cities_with_commas = kwargs.get('cities')
        cities_list = cities_with_commas.split(',')
        api_key = 'd5478237dac7aa890c813beb9e3cc206'
        temperature_sum = float()

        for city in cities_list:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url=url)
            if response.status_code == 200:
                weather_data = response.json()
                temperature_sum += weather_data['main']['temp']

        average_temperature = temperature_sum/len(cities_list)
        return Response(data=average_temperature)

class TasksViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

