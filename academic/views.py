from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Academic
from .forms import AcademicForm  # AcademicForm তৈরি করতে হবে

# ----------------------------
@login_required
@permission_required('academic.view_academic', raise_exception=True)
def academic_list(request):
    data = Academic.objects.all()
    return render(request, 'academic/student/list.html', {'data': data})

# ----------------------------
@login_required
@permission_required('academic.view_academic', raise_exception=True)
def academic_faculty(request):
    data = Academic.objects.all()
    return render(request, 'academic/faculty/list.html', {'data': data})

# ----------------------------
@login_required
@permission_required('academic.add_academic', raise_exception=True)
def add_academic(request):
    if request.method == 'POST':
        form = AcademicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academic:academic_faculty')
    else:
        form = AcademicForm()
    return render(request, 'academic/faculty/add.html', {'form': form})

# ----------------------------
@login_required
@permission_required('academic.change_academic', raise_exception=True)
def edit_academic(request, pk):
    academic = get_object_or_404(Academic, pk=pk)
    if request.method == 'POST':
        form = AcademicForm(request.POST, instance=academic)
        if form.is_valid():
            form.save()
            return redirect('academic:academic_faculty')
    else:
        form = AcademicForm(instance=academic)
    return render(request, 'academic/faculty/edit.html', {'form': form})

# ----------------------------
@login_required
@permission_required('academic.change_academic', raise_exception=True)
def academic_admin(request):
    data = Academic.objects.all()
    return render(request, 'academic/admin/list.html', {'data': data})
# ----------------------------