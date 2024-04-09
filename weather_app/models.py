from django.db import models


class Task(models.Model):
    """database model for tasks"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return string representation of task i.e. name"""
        return self.name



