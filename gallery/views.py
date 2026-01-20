from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Photo, Video
from .forms import PhotoForm, VideoForm
from django.db.models import Q

# ========== Gallery Home ==========
def gallery_home(request):
    search_query = request.GET.get('search', '')
    filter_type = request.GET.get('type', 'all')

    photos = Photo.objects.all().order_by('-created_at')
    videos = Video.objects.all().order_by('-created_at')

    if search_query:
        photos = photos.filter(title__icontains=search_query)
        videos = videos.filter(title__icontains=search_query)

 # Type filter
    if filter_type == 'photo':
        videos = Video.objects.none()
    elif filter_type == 'video':
        photos = Photo.objects.none()

    # Combined list for pagination
    combined = list(photos) + list(videos)
    paginator = Paginator(combined, 10)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery/gallery_home.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'filter_type': filter_type
    })
    
# ---------- ADD ----------
def photo_add(request):
     if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery_home')
     else:
        form = PhotoForm()
     return render(request, 'gallery/form.html', {'form': form, 'title': 'Add Photo'})

def photo_list(request):
     photos = Photo.objects.all()
     return render(request, 'gallery/photo_list.html', {'photos': photos})
 
def video_add(request):
     if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery_home')
     else:
        form = VideoForm()
     return render(request, 'gallery/form.html', {'form': form, 'title': 'Add Video'})


# ========== Photo CRUD ==========
def photo_detail(request, pk):
      photo = get_object_or_404(Photo, pk=pk)
      return render(request, 'gallery/photo_detail.html', {'photo': photo})


def photo_update(request, pk):
    photo = get_object_or_404(Photo, pk=pk)  # যেই photo update করতে চাই
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('gallery:photo_list')  # update হলে কোথায় যাবে
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

