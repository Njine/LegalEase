from django.contrib import admin
from .models import PermissionLevel, SecurityGroup

# Register your models here.
admin.site.register(PermissionLevel) # Register the Security model
admin.site.register(SecurityGroup) # Register the SecurityType model