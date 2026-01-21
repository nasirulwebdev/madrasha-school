# routine/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Routine
from .forms import RoutineForm
from routine import models
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.db.models import Q

def routine_list(request):
    routines = Routine.objects.all().order_by('-created_at')
    return render(request, 'routine/routine_list.html', {'routines': routines})

# Admin/Faculty
class RoutineListView(ListView):
    model = Routine
    template_name = "routine/routine_list.html"
    context_object_name = "routines"
    paginate_by = 5
    ordering = ["-created_at"]

    def get_queryset(self):
        qs = Routine.objects.all().order_by('-created_at')
        search_query = self.request.GET.get("search", "")
        class_filter = self.request.GET.get("class", "")
        day_filter = self.request.GET.get("day", "")

        if day_filter:
            qs = qs.filter(day__iexact=day_filter)
        if class_filter:
            qs = qs.filter(class_name__iexact=class_filter)
        if search_query:
            qs = qs.filter(
                Q(title__icontains=search_query) |
                Q(subject__icontains=search_query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        context["class_filter"] = self.request.GET.get("class", "")
        context["day_filter"] = self.request.GET.get("day", "")
        context["class_options"] = [f"Class {i}" for i in range(1, 13)]
        return context

# Student
@method_decorator(login_required, name="dispatch")
class StudentRoutineListView(ListView):
    model = Routine
    template_name = "routine/student_routine_list.html"
    context_object_name = "routines"
    paginate_by = 5
    ordering = ["day", "start_time"]

    def get_queryset(self):
        class_filter = self.request.GET.get("class", None)
        search_query = self.request.GET.get("search", "")
        day_filter = self.request.GET.get("day", "")

        qs = Routine.objects.all().order_by("day", "start_time")

        if class_filter:
            qs = qs.filter(class_name__iexact=class_filter)

        if search_query:
            qs = qs.filter(
                Q(title__icontains=search_query) |
                Q(subject__icontains=search_query) |
                Q(teacher__icontains=search_query)
            )

        if day_filter:
            qs = qs.filter(day__iexact=day_filter)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        context["day_filter"] = self.request.GET.get("day", "")
        context["class_filter"] = self.request.GET.get("class", "")
        context["class_options"] = [f"Class {i}" for i in range(1,13)]
        return context

def routine_create(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('routine:routine_list')

    else:
        form = RoutineForm()
    return render(request, 'routine/routine_form.html', {'form': form})


def routine_update(request, pk):
    routine = get_object_or_404(Routine, pk=pk)
    if request.method == 'POST':
        form = RoutineForm(request.POST, instance=routine)
        if form.is_valid():
            form.save()
            return redirect('routine:routine_list')

    else:
        form = RoutineForm(instance=routine)
    return render(request, 'routine/routine_form.html', {'form': form})


def routine_delete(request, pk):
    routine = get_object_or_404(Routine, pk=pk)
    if request.method == 'POST':
        routine.delete()
        return redirect('routine:routine_list')

    return render(request, 'routine/routine_confirm_delete.html', {'routine': routine})
