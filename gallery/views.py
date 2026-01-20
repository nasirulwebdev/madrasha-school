from django.views.generic import ListView
from django.shortcuts import render
from .models import Photo, Video

def gallery_home(request):
    return render(request, 'gallery/base.html')



def photo_gallery(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'gallery/photo.html', {'photos': photos})


def video_gallery(request):
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'gallery/video.html', {'videos': videos})

class VideoListView(ListView):
    model = Video
    template_name = 'gallery/video.html'
    context_object_name = 'videos'
    ordering = ['-created_at']
    
class PhotoListView(ListView):
    model = Photo
    template_name = 'gallery/photo.html'
    context_object_name = 'photos'
    ordering = ['-created_at']
    