from django.db import models
from apps.baselayer.basemodels import LogsMixin
from apps.task.enums import TaskStatusChoices

# Create your models here.

class Task(LogsMixin):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(
        choices=TaskStatusChoices.choices, default=TaskStatusChoices.TODO
    )
