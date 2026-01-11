from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Member
from .forms import MemberForm   # update form


class MemberListView(ListView):
    model = Member
    template_name = 'school/members.html'   # ✅ তোমার folder অনুযায়ী
    context_object_name = 'members'
    paginate_by = 8

    def get_queryset(self):
        queryset = Member.objects.all()
        member_type = self.request.GET.get('member_type')
        search = self.request.GET.get('search')
        
        if member_type:
            queryset = queryset.filter(member_type__iexact=member_type)
        if search:
            queryset = queryset.filter(name__icontains=search)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_type'] = self.request.GET.get('member_type')
        context['search_query'] = self.request.GET.get('search', '')
        return context

def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm()
    return render(request, 'school/member_form.html', {'form': form})
# 🔹 MEMBER DETAIL
def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'school/members_detail.html', {
        'member': member
    })


# 🔹 MEMBER UPDATE
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members_detail', pk=pk)
    else:
        form = MemberForm(instance=member)

    return render(request, 'school/members_update.html', {
        'form': form,
        'member': member
    })


# 🔹 MEMBER DELETE (confirmation)
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        member.delete()
        return redirect('members')

    return render(request, 'school/members_confirm_delete.html', {
        'member': member
    })
