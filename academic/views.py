# academic/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Academic
from .forms import AcademicForm

# ----------------------------
# Student List
class AcademicStudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Academic
    template_name = 'academic/student/list.html'
    context_object_name = 'data'
    permission_required = 'academic.view_academic'

# ----------------------------
# Faculty List
class AcademicFacultyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Academic
    template_name = 'academic/faculty/list.html'
    context_object_name = 'data'
    permission_required = 'academic.view_academic'

# ----------------------------
# Add Academic
class AcademicCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Academic
    form_class = AcademicForm
    template_name = 'academic/faculty/add.html'
    permission_required = 'academic.add_academic'
    success_url = reverse_lazy('academic:academic_faculty')

# ----------------------------
# Edit Academic
class AcademicUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Academic
    form_class = AcademicForm
    template_name = 'academic/faculty/edit.html'
    permission_required = 'academic.change_academic'
    success_url = reverse_lazy('academic:academic_faculty')

# ----------------------------
# Admin List
class AcademicAdminListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Academic
    template_name = 'academic/admin/list.html'
    context_object_name = 'data'
    permission_required = 'academic.change_academic'
