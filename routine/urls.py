# routine/urls.py
from django.urls import path, include
from . import views


app_name = 'routine' 

urlpatterns = [
    path('', views.routine_list, name='routine_list'),
    path('create/', views.routine_create, name='routine_create'),
    path('update/<int:pk>/', views.routine_update, name='routine_update'),
    path('delete/<int:pk>/', views.routine_delete, name='routine_delete'),
]
