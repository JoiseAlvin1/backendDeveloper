from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from .utils import get_weather, get_average_temperature

class WeatherAPIView(APIView):
    def get(self, request, city):
        weather_data = get_weather(city)
        return Response(weather_data, status=status.HTTP_200_OK)
    
class AverageTemperatureAPIView(APIView):
    def get(self, request, city_list):
        cities = city_list.split(',')
        average_temperature = get_average_temperature(cities)
        if average_temperature is not None:
            return Response({'average_temperature': average_temperature})
        else:
            return Response({'message': 'No temperature data available for provided cities'}, status=status.HTTP_404_NOT_FOUND)

class TaskListAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAPIView(APIView):

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)