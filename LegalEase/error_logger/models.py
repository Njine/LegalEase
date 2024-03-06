from django.db import models

# Create your models here.

class ErrorLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    error_message = models.TextField()

    def __str__(self):
        return f"Error at {self.timestamp}: {self.error_message}"