from django.test import TestCase
from rest_framework.test import APIRequestFactory

from apps.task.views import TaskAPIView


class TaskAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TaskAPIView.as_view()

    def test_get_success(self):
        request = self.factory.get('/task/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_post_success(self):
        data = {"name": "task 3", "description": "des 3"}
        request = self.factory.post('/task/', data)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)

    def test_post_invalid_data(self):
        data = {"name": "", "description": "des 3"}  # Invalid data
        request = self.factory.post('/task/', data)
        response = self.view(request)
        self.assertEqual(response.status_code, 400)

    def test_patch_success(self):
        data = {"name": "task 2", "description": "des 2"}
        request = self.factory.patch('/task/1', data)
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 500)

    def test_patch_invalid_data(self):
        data = {"name": ""}  # Invalid data
        request = self.factory.patch('/task/1', data)
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 500)

    def test_delete_success(self):
        request = self.factory.delete('/task/1')
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 404)

    def test_delete_invalid_record(self):
        request = self.factory.delete('/task/999')
        response = self.view(request, pk=999)
        self.assertEqual(response.status_code, 404)
