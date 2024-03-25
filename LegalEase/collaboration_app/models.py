from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('auth.User')

    def __str__(self):
        return self.name
