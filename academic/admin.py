from django.contrib import admin
from .models import Academic

class AcademicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'designation',
        'department',
        'email',
        'year',
    )

    search_fields = (
        'name',
        'email',
        'department',
    )

    list_filter = (
        'department',
        'year',
        'name',
        'email',
    )

    ordering = ('name',)

admin.site.register(Academic, AcademicAdmin)



