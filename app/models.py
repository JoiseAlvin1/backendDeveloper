from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title