from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberListView.as_view(), name='members'),   # 👈 list page
    path('add/', views.member_create, name='members_create'),
    path('<int:pk>/', views.member_detail, name='members_detail'),
    path('<int:pk>/update/', views.member_update, name='members_update'),
    path('<int:pk>/delete/', views.member_delete, name='members_delete'),
]
