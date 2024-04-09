import pytest
from app.models import Task


@pytest.mark.django_db
def test_create_task():
    task = Task.objects.create(title='Test Task', description='This is a test task')
    assert task.title == 'Test Task'
    assert task.description == 'This is a test task'

@pytest.mark.django_db
def test_task_str():
    task = Task.objects.create(title='Test Task', description='This is a test task')
    assert str(task) == 'Test Task'
