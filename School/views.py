from django.apps import AppConfig
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # pyright: ignore[reportMissingModuleSource]
from members.models import Member



# Function-based view
def home(request):
    return HttpResponse("")

# Class-based views
class AbcView(TemplateView):
    template_name = "School/abc.html"

class AboutView(TemplateView):
    template_name = "School/about.html"

class BaseView(TemplateView):
    template_name = "School/base.html"
   
 

class MembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'

   