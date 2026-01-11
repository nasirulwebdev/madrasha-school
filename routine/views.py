# routine/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Routine
from .forms import RoutineForm
from routine import models

def routine_list(request):
    routines = Routine.objects.all().order_by('-created_at')
    return render(request, 'routine/routine_list.html', {'routines': routines})

def routine_list(request):
    # Get filter values from GET request
    day_filter = request.GET.get('day', '')
    class_filter = request.GET.get('class', '')
    search_query = request.GET.get('search', '')
    # Get all routines
    routines = Routine.objects.all().order_by('-created_at')

    # Apply filters if provided
    if day_filter:
        routines = routines.filter(day__iexact=day_filter)
    if class_filter:
        routines = routines.filter(class_name__iexact=class_filter)
    if search_query:
        routines = routines.filter(
            models.Q(title__icontains=search_query) |
            models.Q(subject__icontains=search_query)
        )
    return render(request, 'routine/routine_list.html', {
        'routines': routines,
        'day_filter': day_filter,
        'class_filter': class_filter,
        'search_query': search_query,  # pass to template
    })

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
