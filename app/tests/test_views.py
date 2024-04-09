import pytest
from rest_framework.test import APIClient
from app.models import Task


@pytest.mark.django_db
def test_create_task_api():
    client = APIClient()
    response = client.post('/tasks/', {'title': 'Test Task', 'description': 'This is a test task'})
    assert response.status_code == 201

@pytest.mark.django_db
def test_get_task_api():
    task = Task.objects.create(title='Test Task', description='This is a test task')
    client = APIClient()
    response = client.get(f'/tasks/{task.pk}/')
    assert response.status_code == 200
    assert response.data['title'] == 'Test Task'

@pytest.mark.django_db
def test_update_task_api():
    task = Task.objects.create(title='Test Task', description='This is a test task')
    client = APIClient()
    response = client.put(f'/tasks/{task.pk}/', {'title': 'Updated Task', 'description': 'This is an updated task'})
    assert response.status_code == 200
    assert response.data['title'] == 'Updated Task'

@pytest.mark.django_db
def test_delete_task_api():
    task = Task.objects.create(title='Test Task', description='This is a test task')
    client = APIClient()
    response = client.delete(f'/tasks/{task.pk}/')
    assert response.status_code == 204
    assert not Task.objects.filter(pk=task.pk).exists()

# @pytest.mark.django_db
# def test_get_weather_api():
#     client = APIClient()
#     response = client.get('/weather/Islamabad/')
#     assert response.status_code == 200
#     assert 'weather' in response.data
#     assert 'main' in response.data

# @pytest.mark.django_db
# def test_get_average_temperature_api():
#     client = APIClient()
#     response = client.get('/average_temperature/Islamabad,Karachi/')
#     assert response.status_code == 200
#     assert 'average_temperature' in response.data
