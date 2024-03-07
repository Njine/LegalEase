from django.shortcuts import render, get_object_or_404
from .models import User

def user_list(request):
    """View function for listing users."""
    users = User.objects.all()
    return render(request, 'user_app/user_list.html', {'users': users})

def user_detail(request, user_id):
    """View function for displaying user details."""
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_app/user_detail.html', {'user': user})
