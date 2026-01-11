from django.urls import path
from . import views

urlpatterns = [
    path('', views.academic_list, name='academic_list'),
]
