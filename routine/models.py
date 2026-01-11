# routine/models.py
from django.db import models

class Routine(models.Model):
    class_name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    day = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
