from django.urls import path
from .views import (
    NoticeListView,
    NoticeDetailView,
    NoticeCreateView,
    NoticeUpdateView,
    NoticeDeleteView,
)

app_name = "notice"

urlpatterns = [
    path('', NoticeListView.as_view(), name='notice_list'),   # 👈 এখানে নাম "notice"
    path('add/', NoticeCreateView.as_view(), name='notice_create'),
    path('<int:pk>/', NoticeDetailView.as_view(), name='notice_detail'),
    path('<int:pk>/update/', NoticeUpdateView.as_view(), name='notice_update'),
    path('<int:pk>/delete/', NoticeDeleteView.as_view(), name='notice_delete'),
]