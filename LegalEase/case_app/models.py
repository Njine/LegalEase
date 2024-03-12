from django.db import models
from user_app.models import UserProfile  # Import UserProfile model
from document_app.models import Document  # Import Document model

class CourtLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Case(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    court_level = models.ForeignKey(CourtLevel, on_delete=models.CASCADE)
    judge_or_arbitrator = models.CharField(max_length=100)
    scheduling_date = models.DateTimeField()
    lawyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Use UserProfile model
    documents = models.ManyToManyField('document_app.Document')  # Use Document model

    def __str__(self):
        return self.title
