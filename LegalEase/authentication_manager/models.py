from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('partner', 'Partner'), ('associate', 'Associate'), ('clerk', 'Clerk'), ('secretary', 'Secretary'), ('admin', 'Admin')])

    def __str__(self):
        return f"{self.user.username} - {self.role}"
