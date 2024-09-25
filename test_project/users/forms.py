from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birth_date', 'image']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }