from django.shortcuts import render
from .models import Academic

def academic_list(request):
    data = Academic.objects.all()
    return render(request, 'academic/academic_list.html', {'data': data})