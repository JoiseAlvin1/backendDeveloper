from rest_framework import serializers
from .models import Task


class TasksSerializer(serializers.ModelSerializer):
    """Serializer for Task objects"""
    class Meta:
        """MetaClass for binding the serializer to Task model"""
        model = Task
        fields = '__all__'


