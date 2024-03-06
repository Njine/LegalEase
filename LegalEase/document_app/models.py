from django.db import models
from case_app.models import Case

class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file_path = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
