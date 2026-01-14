from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description', 'notice_date', 'class_name', 'day']
        widgets = {
            'notice_date': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'class_name': forms.Select(attrs={'class':'form-select'}),
            'day': forms.Select(attrs={'class':'form-select'}),
        }
