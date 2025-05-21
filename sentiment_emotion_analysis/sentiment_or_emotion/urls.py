from django.urls import path, re_path
from . import views

app_name = 'sentiment_or_emotion'

urlpatterns = [
    re_path(r'^$', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
]
