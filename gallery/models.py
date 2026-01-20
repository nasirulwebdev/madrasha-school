from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='gallery/videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title