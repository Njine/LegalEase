from django.db import models
from user_app.models import CustomUser  # Import CustomUser model
from document_app.models import Document  # Import Document model

class CourtType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Court(models.Model):
    name = models.CharField(max_length=100)
    court_type = models.ForeignKey(CourtType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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
    lawyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser model
    documents = models.ManyToManyField(Document)  # Use Document model
    court = models.ForeignKey(Court, on_delete=models.CASCADE, default=1)
    start_date = models.DateField(default=None)  # Add default value
    end_date = models.DateField(default=None)  # Add default value

    def __str__(self):
        return self.title
