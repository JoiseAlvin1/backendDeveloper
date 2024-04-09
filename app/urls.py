from django.urls import path
from .views import GenerateAPIKey, TaskListAPIView, TaskDetailAPIView, WeatherAPIView, AverageTemperatureAPIView


urlpatterns = [
    path('generate-api-key/', GenerateAPIKey.as_view(), name='generate_api_key'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('weather/<str:city>/', WeatherAPIView.as_view(), name='weather'),
    path('average_temperature/<str:city_list>/', AverageTemperatureAPIView.as_view(), name='average-temperature'),
]