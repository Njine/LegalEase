from django.db import models

# Create your models here.

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    legal_representation = models.ForeignKey('Lawyer', on_delete=models.CASCADE)