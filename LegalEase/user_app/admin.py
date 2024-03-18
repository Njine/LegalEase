from django.contrib import admin
from .models import CustomUser

# Register CustomUser model with the admin site
admin.site.register(CustomUser)
