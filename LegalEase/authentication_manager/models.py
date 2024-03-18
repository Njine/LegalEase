from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission  

class User(AbstractUser):
    ROLES = (
        ('partner', 'Partner'),
        ('associate', 'Associate'),
        ('clerk', 'Clerk'),
        ('secretary', 'Secretary'),
        ('admin', 'Admin'),
    )

    is_admin = models.BooleanField(default=False)

    def create_user(self, username, password, role):
        user = User.objects.create_user(username=username, password=password)
        user.role = role
        user.save()
        return user
    role = models.CharField(max_length=20, choices=ROLES)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='auth_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='auth_user_permissions')
