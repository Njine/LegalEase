from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput,
        help_text="Enter your old password."
    )
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput,
        help_text="Enter your new password. It must be at least 8 characters long."
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput,
        help_text="Enter the same password as before, for verification."
    )

    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')
