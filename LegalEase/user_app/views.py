from django.shortcuts import render, get_object_or_404
from .models import CustomUser

def user_profile_list(request):
    """View function for listing user profiles."""
    profiles = CustomUser.objects.all()
    return render(request, 'user_app/user_profile_list.html', {'profiles': profiles})

def user_profile_detail(request, user_id):
    """View function for displaying user profile details."""
    profile = get_object_or_404(CustomUser, user__id=user_id)
    return render(request, 'user_app/user_profile_detail.html', {'profile': profile})
