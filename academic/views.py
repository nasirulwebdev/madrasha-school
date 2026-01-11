from django.shortcuts import render
from .models import Academic

def academic_list(request):
    academics = Academic.objects.all()
    return render(request, 'academic/academic_list.html', {'academics': academics})
