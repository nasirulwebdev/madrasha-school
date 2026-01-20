from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.db.models import Q
from notice.models import Notice


class NoticeListView(ListView):
    template_name = "notice/notice_list.html"
    model = Notice
    context_object_name = "notices"
    paginate_by = 8
    ordering = ["-created_at"]

    def get_queryset(self):
        print("🔥 SEARCH VIEW HIT 🔥")
        qs = super().get_queryset()

        day = self.request.GET.get('day')
        class_name = self.request.GET.get('class')
        search = self.request.GET.get('search')

        if day:
            qs = qs.filter(day__iexact=day)

        if class_name:
            qs = qs.filter(class_name__iexact=class_name)

        if search:
            qs = qs.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['day_filter'] = self.request.GET.get('day', '')
        context['class_filter'] = self.request.GET.get('class', '')
        context['search_query'] = self.request.GET.get('search', '')
        return context

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
