from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=150)
    caption = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.TimeField(default=datetime.now())

    def __str__(self):
        return self.title