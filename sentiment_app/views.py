from django.shortcuts import render
from django.http import JsonResponse
from .services import SentimentAnalyzer
from .models import TweetAnalysis

analyzer = SentimentAnalyzer()

def home(request):
    return render(request, 'sentiment_app/home.html')

def analyze_tweet(request):
    if request.method == 'POST':
        tweet_text = request.POST.get('tweet_text', '')
        if tweet_text:
            analysis = analyzer.analyze_tweet(tweet_text)
            
            # Save the analysis
            TweetAnalysis.objects.create(
                tweet_text=tweet_text,
                sentiment=analysis['sentiment'],
                emotion=analysis['emotion']
            )
            
            return JsonResponse({
                'success': True,
                'sentiment': analysis['sentiment'],
                'emotion': analysis['emotion']
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def search_tweets(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        if query:
            tweets = analyzer.search_tweets(query)
            return JsonResponse({
                'success': True,
                'tweets': tweets
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})
