from .models import Photo, Video

def gallery_menu(request):
    return {
        'menu_photos': Photo.objects.all(),
        'menu_videos': Video.objects.all(),
    }
