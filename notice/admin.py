from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'class_name', 'day', 'notice_date', 'created_at')
    list_filter = ('class_name', 'day')
    search_fields = ('title', 'description')
