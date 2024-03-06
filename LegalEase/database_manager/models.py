from django.db import models

class DatabaseLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.message}"
