from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UserLoginForm(AuthenticationForm):
    # Additional fields or customizations
    remember_me = forms.BooleanField(required=False, label='Remember Me')
    # You can add more fields as needed
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can customize the form further, such as adding placeholders or CSS classes
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
            self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'
            self.fields['remember_me'].widget.attrs['class'] = 'form-check-input'

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'authentication_manager/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_profile(request):
    return render(request, 'authentication_manager/profile.html')
