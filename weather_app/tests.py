from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task


class WeatherDataAPITestCase(TestCase):
    """
    Test case for verifying successful request to fetch
    weather data for a given city
    """

    def test_weather_data_api(self):
        client = APIClient()
        response = client.get('/weather/Karachi')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AverageWeatherDataAPITestCase(TestCase):
    """
    Test case for verifying successful request to calculate
    average temperature for the given list of cities
    """

    def test_average_weather_data_api(self):
        client = APIClient()
        response = client.get('/average_temperature/Lahore,Karachi,Islamabad')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TasksViewSetTestCase(TestCase):
    """
    Test cases for verifying successful CRUD operations
    on the Task database model using ViewSet endpoints
    """

    def setUp(self):
        self.client = APIClient()
        self.task_data = {'name': 'Test Task', 'description': 'This is a test task.'}
        self.task = Task.objects.create(name='Existing Task', description='This is an existing task.')

    def test_task_list(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        response = self.client.post('/tasks', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_task(self):
        response = self.client.get(f'/tasks/{self.task.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        updated_data = {'name': 'Updated Task', 'description': 'This is an updated task.'}
        response = self.client.put(f'/tasks/{self.task.id}', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(f'/tasks/{self.task.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)