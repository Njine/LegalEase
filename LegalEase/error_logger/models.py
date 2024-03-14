from django.db import models

class ErrorLog(models.Model):
    error_message = models.TextField()
    error_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
