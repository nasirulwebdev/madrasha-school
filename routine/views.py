# routine/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Routine
from .forms import RoutineForm

def routine_list(request):
    routines = Routine.objects.all().order_by('-created_at')
    return render(request, 'routine/routine_list.html', {'routines': routines})


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
