from django.db import models


class TaskStatusChoices(models.IntegerChoices):
    TODO = 1, "Todo"
    IN_PROGRESS = 2, "In Progress"
    COMPLETED = 3, "Completed"
    IN_COMPLETE = 4, "In Complete"
