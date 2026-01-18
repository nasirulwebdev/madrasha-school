# academic/forms.py
from django import forms
from .models import Academic
from django.core.exceptions import ValidationError

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
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # ✅ add this
        }


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@school.edu'):
            raise forms.ValidationError("Email must be from the domain '@school.edu'")
        return email

     # ✅ Image validation
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            valid_extensions = ['jpg', 'jpeg', 'png']
            ext = image.name.split('.')[-1].lower()
            if ext not in valid_extensions:
                raise ValidationError('Only .jpg, .jpeg, .png files are allowed.')
        return image