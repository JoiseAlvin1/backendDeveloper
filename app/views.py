from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from .tasks import get_weather, get_average_temperature

class WeatherAPIView(APIView):
    def get(self, request, city):
        cache_key = f'weather_{city}'
        weather_data = cache.get(cache_key)
        if not weather_data:
            weather_data = get_weather.delay(city).get()
            cache.set(cache_key, weather_data)
        return Response(weather_data, status=status.HTTP_200_OK)
    
class AverageTemperatureAPIView(APIView):
    def get(self, request, city_list):
        cache_key = f'average_temperature_{city_list}'
        average_temperature = cache.get(cache_key)
        if average_temperature is None:
            cities = city_list.split(',')
            average_temperature = get_average_temperature.delay(cities).get()
            cache.set(cache_key, average_temperature)
        if average_temperature is not None:
            return Response({'average_temperature': average_temperature}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No temperature data available for provided cities'}, status=status.HTTP_404_NOT_FOUND)

class TaskListAPIView(APIView):
    def get(self, request):
        cache_key = f'task_list'
        data = cache.get(cache_key)
        if data is None:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            data = serializer.data
            cache.set(cache_key, data)
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete('task_list')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAPIView(APIView):
    def get(self, request, pk):
        cache_key = f'task_{pk}'
        data = cache.get(cache_key)
        if data is None:
            task = get_object_or_404(Task, pk=pk)
            serializer = TaskSerializer(task)
            data = serializer.data
            cache.set(cache_key, data)
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            cache.set(f'task_{pk}', data)
            cache.delete('task_list')
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        cache.delete(f'task_{pk}')
        cache.delete('task_list')
        return Response(status=status.HTTP_204_NO_CONTENT)