from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Academic
from .forms import AcademicForm

# ----------------------------
# Student List (students can see teachers/admins)
class AcademicStudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Academic
    template_name = 'academic/student/list.html'
    context_object_name = 'data'
    permission_required = 'academic.view_academic'
    paginate_by = 10   # ✅ pagination
    
    def get_queryset(self):
        queryset = Academic.objects.exclude(designation='Student')  # only teacher/admin
        search = self.request.GET.get('search')
        year = self.request.GET.get('year')
        email = self.request.GET.get('email')
        if search:
            queryset = queryset.filter(name__icontains=search)
        if year:
            queryset = queryset.filter(year=year)
        if email:
            queryset = queryset.filter(email=email)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # dropdown values
        context['years'] = Academic.objects.exclude(designation='Student').values_list('year', flat=True).distinct()
        context['emails'] = Academic.objects.exclude(designation='Student').values_list('email', flat=True).distinct()
        return context
# ----------------------------
# Faculty List (teachers/admins)
class AcademicFacultyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Academic
    template_name = 'academic/faculty/list.html'
    context_object_name = 'data'
    permission_required = 'academic.view_academic'
    paginate_by = 10   # ✅ pagination
    
    def get_queryset(self):
        queryset = Academic.objects.exclude(designation='Student')  # show only teacher/admin
        search = self.request.GET.get('search')
        year = self.request.GET.get('year')
        email = self.request.GET.get('email')

        if search:
            queryset = queryset.filter(name__icontains=search)
        if year:
            queryset = queryset.filter(year=year)
        if email:
            queryset = queryset.filter(email__icontains=email)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = Academic.objects.values_list('year', flat=True).distinct()
        context['emails'] = Academic.objects.values_list('email', flat=True).distinct()
        return context

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
# Delete Academic
class AcademicDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Academic
    template_name = 'academic/faculty/delete.html'
    permission_required = 'academic.delete_academic'
    success_url = reverse_lazy('academic:academic_admin')

# ----------------------------
# Admin List (admins can see everyone)
class AcademicAdminListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Academic
    template_name = 'academic/admin/list.html'
    context_object_name = 'data'
    permission_required = 'academic.change_academic'
    paginate_by = 10   # ✅ pagination
    
    def get_queryset(self):
        queryset = Academic.objects.all()
        search = self.request.GET.get('search')
        year = self.request.GET.get('year')
        email = self.request.GET.get('email')

        if search:
            queryset = queryset.filter(name__icontains=search)
        if year:
            queryset = queryset.filter(year=year)
        if email:
            queryset = queryset.filter(email__icontains=email)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Template-এ filter dropdown এর জন্য distinct values পাঠানো
        context['years'] = Academic.objects.values_list('year', flat=True).distinct()
        context['emails'] = Academic.objects.values_list('email', flat=True).distinct()
        return context
