# emotion/models.py
from django.db import models

class Tweet(models.Model):
    content = models.CharField(max_length=280)
    emotion = models.CharField(max_length=100)
