from django.db import models

# Create your models here.

class Case(models.Model):
    case_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField()
    assigned_lawyer = models.ForeignKey('Lawyer', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed')])