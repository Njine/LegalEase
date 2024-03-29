from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserForm

@login_required
def user_list(request):
    """View function for listing users."""
    users = CustomUser.objects.all()
    return render(request, 'user_app/user_list.html', {'users': users})

@login_required
def user_detail(request, user_id):
    """View function for displaying details of a single user."""
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_app/user_detail.html', {'user': user})

@login_required
def create_user(request):
    """View function for creating a new user."""
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserForm()
    return render(request, 'user_app/user_form.html', {'form': form})

@login_required
def update_user(request, user_id):
    """View function for updating an existing user."""
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user_id)
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'user_app/user_form.html', {'form': form})
