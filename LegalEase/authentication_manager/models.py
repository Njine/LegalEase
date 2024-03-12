from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission  
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    ROLES = (
        ('partner', 'Partner'),
        ('associate', 'Associate'),
        ('clerk', 'Clerk'),
        ('secretary', 'Secretary'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    # Add related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='custom_user_set')
