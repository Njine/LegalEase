from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    """View function for handling user login."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'authentication_manager/login.html')

def user_logout(request):
    """View function for handling user logout."""
    logout(request)
    return redirect('login')

def user_profile(request):
    """View function for displaying user profile."""
    return render(request, 'authentication_manager/profile.html')
