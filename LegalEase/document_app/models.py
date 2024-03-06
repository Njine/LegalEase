from django.db import models

# Create your models here.

class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file_path = models.FileField(upload_to='documents/')
    associated_case = models.ForeignKey(Case, on_delete=models.CASCADE)