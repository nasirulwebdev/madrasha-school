
from django.db import models

# Create your models here.
class Member(models.Model):
    MEMBER_TYPE_CHOICES = (
         ('teacher', 'Teacher'),
        ('staff', 'Staff'),
        ('student', 'Student')
    )
    
    member_type = models.CharField(max_length=50, choices=MEMBER_TYPE_CHOICES) # type: ignore
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name