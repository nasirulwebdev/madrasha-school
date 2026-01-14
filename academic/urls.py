from django.urls import path
from . import views

app_name = 'academic'

urlpatterns = [
    path('', views.academic_list, name='academic_list'),
    path('faculty/', views.academic_faculty, name='academic_faculty'),
    path('faculty/add/', views.add_academic, name='add_academic'),
    path('faculty/<int:pk>/edit/', views.edit_academic, name='edit_academic'),
    path('admin/', views.academic_admin, name='academic_admin'),
]

# Note: The 'app_name' variable is crucial for namespacing the URLs of this app.