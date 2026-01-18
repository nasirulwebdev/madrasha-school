from django.db import models

class Academic(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='academic/', blank=True, null=True)  # ✅ এখানে
    def __str__(self):
        return self.name