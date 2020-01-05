from django.db import models

class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.IntegerField()
    date = models.DateTimeField()
    feedback = models.CharField(max_length=500)
