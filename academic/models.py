# academic/models.py
from routine import models


class Academic(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
