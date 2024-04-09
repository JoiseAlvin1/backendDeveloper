from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView, WeatherAPIView, AverageTemperatureAPIView


urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('weather/<str:city>/', WeatherAPIView.as_view(), name='weather'),
    path('average_temperature/<str:city_list>/', AverageTemperatureAPIView.as_view(), name='average-temperature'),
]