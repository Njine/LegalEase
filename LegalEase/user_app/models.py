from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('partner', 'Partner'), ('associate', 'Associate'), ('clerk', 'Clerk'), ('secretary', 'Secretary'), ('admin', 'Admin')])

    class Meta:
        app_label = 'user_app'  # Add this line

    def __str__(self):
        return f"{self.user.username} - {self.role}"
