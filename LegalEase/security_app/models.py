from django.db import models

class PermissionLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SecurityGroup(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(PermissionLevel)

    def __str__(self):
        return self.name
