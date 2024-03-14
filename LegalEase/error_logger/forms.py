from django import forms

class ErrorLogForm(forms.Form):
    error_message = forms.CharField(widget=forms.Textarea)
    error_code = forms.CharField(max_length=50)
