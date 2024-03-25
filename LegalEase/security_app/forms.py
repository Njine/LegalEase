from django import forms
from .models import SecurityGroup

class SecurityGroupForm(forms.ModelForm):
    class Meta:
        model = SecurityGroup
        fields = ['name', 'permissions']
        widgets = {
            'permissions': forms.CheckboxSelectMultiple
        }
