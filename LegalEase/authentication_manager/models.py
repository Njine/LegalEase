from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('partner', 'Partner'),
        ('associate', 'Associate'),
        ('clerk', 'Clerk'),
        ('secretary', 'Secretary'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
