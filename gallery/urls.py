from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
   path('', views.gallery_home, name='gallery_home'),
    path('photos/', views.photo_gallery, name='photo_list'),
    path('videos/', views.video_gallery, name='video_list'),
]
    