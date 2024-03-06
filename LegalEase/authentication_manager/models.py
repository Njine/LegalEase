from django.db import models
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class AuthenticationManager(BaseUserManager):
    def authenticate_user(self, username, password):
        try:
            # Retrieve the user based on the provided username
            user = User.objects.get(username=username)
            # Check if the password matches
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # User does not exist or password is incorrect
            pass
        return None

    def grant_access(self, user):
        # Determine the access privileges based on the user's role
        if user.role == 'partner':
            return 'full_access'
        elif user.role == 'associate':
            return 'limited_access'
        elif user.role == 'clerk':
            return 'limited_access'
        elif user.role == 'secretary':
            return 'limited_access'
        elif user.role == 'admin':
            return 'admin_access'

    def handle_authentication_errors(self, error):
        # Handle authentication errors (e.g., incorrect password)
        # For simplicity, you might log the error or raise an exception
        pass
