# academic/urls.py
from django.urls import path
from .views import (
    AcademicStudentListView,
    AcademicFacultyListView,
    AcademicCreateView,
    AcademicUpdateView,
    AcademicAdminListView,
)

app_name = 'academic'

urlpatterns = [
    path('', AcademicStudentListView.as_view(), name='academic_list'),
    path('faculty/', AcademicFacultyListView.as_view(), name='academic_faculty'),
    path('add/', AcademicCreateView.as_view(), name='add_academic'),
    path('edit/<int:pk>/', AcademicUpdateView.as_view(), name='edit_academic'),
    path('admin/', AcademicAdminListView.as_view(), name='academic_admin'),
]
