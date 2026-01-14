from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from notice.models import Notice

class NoticeListView(ListView):
    template_name = "notice/notice_list.html"
    model = Notice
    context_object_name = "notices"
    paginate_by = 8
    ordering = ["-created_at"]

class NoticeDetailView(DetailView):
    template_name = "notice/notice_detail.html"
    model = Notice
    context_object_name = "notice"

class NoticeCreateView(CreateView):
    template_name = "notice/notice_form.html"
    model = Notice
    fields = ["title", "description", "notice_date", "class_name", "day"]  # ✅ added class_name + day
    success_url = reverse_lazy("notice:notice_list")
    extra_context = {"page_title": "Add Notice"}

class NoticeUpdateView(UpdateView):
    model = Notice
    fields = ["title", "description", "notice_date", "class_name", "day"]  # ✅ added class_name + day
    template_name = "notice/notice_form.html"
    success_url = reverse_lazy("notice:notice_list")
    extra_context = {"page_title": "Edit Notice"}

class NoticeDeleteView(DeleteView):
    model = Notice
    template_name = "notice/notice_confirm_delete.html"
    success_url = reverse_lazy("notice:notice_list")
    context_object_name = "notice"
