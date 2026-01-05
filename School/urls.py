from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    # members app urls
    path('members/', include('members.urls')),

    # home page
    path('', home, name='home'),

    # static pages
    path('abc/', TemplateView.as_view(template_name='School/abc.html'), name='abc'),
    path('about/', TemplateView.as_view(template_name='School/about.html'), name='about'),
    path('base/', TemplateView.as_view(template_name='School/base.html'), name='base'),
   
   
     # members app urls
    path('notice/', include('notice.urls', namespace='notice')),

    # home page
    path('', home, name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
