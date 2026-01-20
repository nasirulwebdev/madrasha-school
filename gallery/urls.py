from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
        
    
    # Photo CRUD
    path('photo/', views.photo_list, name='photo_list'),
    path('photo/add/', views.photo_add, name='photo_add'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/update/', views.photo_update, name='photo_update'),
    path('photo/<int:pk>/delete/', views.photo_delete, name='photo_delete'),

    # Video CRUD
    path('video/add/', views.video_add, name='video_add'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('video/<int:pk>/update/', views.video_update, name='video_update'),
    path('video/<int:pk>/delete/', views.video_delete, name='video_delete'),
]
    