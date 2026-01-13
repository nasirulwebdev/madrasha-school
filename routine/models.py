# routine/models.py
from django.db import models

CLASS_CHOICES = [
        ('Class 1', 'Class 1'),
        ('Class 2', 'Class 2'),
        ('Class 3', 'Class 3'),
        ('Class 4', 'Class 4'),
        ('Class 5', 'Class 5'),
        ('Class 6', 'Class 6'),
        ('Class 7', 'Class 7'),
        ('Class 8', 'Class 8'),
        ('Class 9', 'Class 9'),
        ('Class 10', 'Class 10'),
        ('Class 11', 'Class 11'),
        ('Class 12', 'Class 12'),
        # Add more classes as needed
    ]

DAY_CHOICES = [
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
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
        return f"{self.title} - {self.class_name} - {self.day}"
