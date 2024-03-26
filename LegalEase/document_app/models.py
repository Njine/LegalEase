from django.db import models
from django.contrib.auth.models import User

class DocumentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

VISIBILITY_CHOICES = (
    ('public', 'Public'),
    ('private', 'Private'),
)

class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, default=3)  # Set default value to 3
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')
    tags = models.ManyToManyField(Tag)
    file_path = models.FileField(upload_to='documents/')
    content = models.TextField(default='please add content here')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set default value to 1

    def __str__(self):
        return self.title
