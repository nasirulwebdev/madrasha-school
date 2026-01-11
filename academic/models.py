from django.db import models

class Academic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.title