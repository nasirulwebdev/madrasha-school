# academic/forms.py
from django import forms
from .models import Academic

class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academic
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@school.edu'):
            raise forms.ValidationError("Email must be from the domain '@school.edu'")
        return email
