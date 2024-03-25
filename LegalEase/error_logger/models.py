from django.db import models

class ErrorLogger(models.Model):
    error_message = models.TextField()
    error_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    error_severity = models.CharField(max_length=50, default='medium')  # Default value set to 'medium'
    error_type = models.CharField(max_length=50, default='general')  # Default value set to 'general'

    def __str__(self):
        return f"Error: {self.error_code} - Type: {self.error_type}"
