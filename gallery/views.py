from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Photo, Video
from .forms import PhotoForm, VideoForm
from django.db.models import Q

# ========== Gallery Home ========== 
def gallery_home(request):
    search_query = request.GET.get('search', '')

    photos = Photo.objects.all()
    videos = Video.objects.all()

    if search_query:
        photos = photos.filter(title__icontains=search_query)
        videos = videos.filter(title__icontains=search_query)

    return render(request, 'gallery/gallery_home.html', {
        'photos': photos,
        'videos': videos,
        'search_query': search_query
    })

# ========== Photo CRUD ==========
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'gallery/photo_detail.html', {'photo': photo})

def photo_update(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery_home')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'gallery/photo_form.html', {'form': form, 'photo': photo})

def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('gallery:gallery_home')
    return render(request, 'gallery/photo_confirm_delete.html', {'photo': photo})

# ========== Video CRUD ==========
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'gallery/video_detail.html', {'video': video})

def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery_home')
    else:
        form = VideoForm(instance=video)
    return render(request, 'gallery/video_form.html', {'form': form, 'video': video})

def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('gallery:gallery_home')
    return render(request, 'gallery/video_confirm_delete.html', {'video': video})

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
    