# routine/admin.py
from django.contrib import admin
from .models import Routine

admin.site.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('title', 'class_name', 'day', 'subject', 'start_time', 'end_time', 'room')
    list_filter = ('class_name', 'day')
    search_fields = ('title', 'subject', 'teacher')