from django.db import models

# Create your models here.

class TweetAnalysis(models.Model):
    SENTIMENT_CHOICES = [
        ('POS', 'Positive'),
        ('NEG', 'Negative'),
        ('NEU', 'Neutral'),
    ]
    
    EMOTION_CHOICES = [
        ('LOVE', 'Love'),
        ('HAP', 'Happiness'),
        ('SAD', 'Sadness'),
        ('WOR', 'Worry'),
    ]
    
    tweet_text = models.TextField()
    sentiment = models.CharField(max_length=3, choices=SENTIMENT_CHOICES)
    emotion = models.CharField(max_length=4, choices=EMOTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tweet_text[:50]}... - {self.get_sentiment_display()}"
