# Import necessary modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Define a custom admin class for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']

# Register the model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
