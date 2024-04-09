"""
URL configuration for WeatherSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weather_app.views import TasksViewSet, WeatherDataAPIView, AverageWeatherDataAPIView
urlpatterns = [
    # urls for performing CRUD operations on the Tasks
    path('tasks', TasksViewSet.as_view({'get':'list','post':'create'}), name='task-list'),
    path('tasks/<int:pk>', TasksViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name='task'),

    # parameterized urls for fetching & performing calculations on data fetched by Open Weather API
    path('weather/<str:city>', WeatherDataAPIView.as_view(), name='city_weather'),
    path('average_temperature/<str:cities>', AverageWeatherDataAPIView.as_view(), name='average_weather'),

    # url for admin portal, not necessary for this project
    path('admin/', admin.site.urls)

]
