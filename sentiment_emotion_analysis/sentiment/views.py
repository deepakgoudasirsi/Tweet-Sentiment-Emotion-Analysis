from django.shortcuts import render, redirect, HttpResponse
from .forms import Sentiment_Typed_Tweet_analyse_form, Sentiment_Imported_Tweet_analyse_form
from .sentiment_analysis_code import sentiment_analysis_code
from .tweepy_sentiment import Import_tweet_sentiment
import pandas as pd

# Assuming you have a CSV file with tweets and emotions
def sentiment_analysis(request):
    # Load the dataset (assuming a CSV for this example)
    dataset = pd.read_csv('/Users/deepakgouda/Downloads/Twitter_Sentiment_Emotion-Analysis/sentiment_emotion_analysis/text_emotion.csv')  # Adjust path accordingly

    # Print the columns to check if they match the expected ones
    print(dataset.columns)

    # Extract the relevant columns ('content' for the tweet text and 'sentiment' for the emotion)
    list_of_tweets_and_sentiments = dataset[['content', 'sentiment']].values.tolist()

    # Prepare the context to send to the template
    context = {
        'list_of_tweets_and_sentiments': list_of_tweets_and_sentiments,
    }

    return render(request, 'home/sentiment.html', context)


def sentiment_analysis_type(request):
    if request.method == 'POST':
        form = Sentiment_Typed_Tweet_analyse_form(request.POST)
        analyze = sentiment_analysis_code()
        if form.is_valid():
            tweet = form.cleaned_data['sentiment_typed_tweet']
            sentiment = analyze.get_tweet_sentiment(tweet)
            context = {
                'tweet': tweet,
                'sentiment': sentiment
            }
            # Render emotion_type_result.html located in the 'home' template directory
            return render(request, 'home/sentiment_type_result.html', context)
    else:
        form = Sentiment_Typed_Tweet_analyse_form()

    # Render emotion_type.html located in the 'home' template directory
    return render(request, 'home/sentiment_type.html', {'form': form})


def sentiment_analysis_import(request):
    if request.method == 'POST':
        form = Sentiment_Imported_Tweet_analyse_form(request.POST)
        analyze = sentiment_analysis_code()
        if form.is_valid():
            handle = form.cleaned_data['sentiment_imported_tweet']
            # Use Import_tweet_emotion function to get tweets for the given handle
            tweet_data = Import_tweet_sentiment(handle)  # Ensure this function fetches relevant tweets for the handle
            
            if not tweet_data:
                return HttpResponse("No tweets found for the provided handle or hashtag.")

            list_of_tweets_and_sentiments = []
            list_of_tweets = tweet_data.get('list_of_tweets', [])

            # Check if the handle starts with a hashtag or '@'
            if handle.startswith('#'):
                list_of_tweets_and_sentiments = []
                # Fetching tweets using hashtag
                for tweet in list_of_tweets:
                    sentiment = analyze.get_tweet_sentiment(tweet)
                    list_of_tweets_and_sentiments.append((tweet, sentiment))
                context = {
                    'list_of_tweets_and_sentiments': list_of_tweets_and_sentiments,
                    'handle': handle
                }
                # Render emotion_import_result_hashtag.html located in the 'home' template directory
                return render(request, 'home/sentiment_import_result_hashtag.html', context)

            elif handle.startswith('@'):
                # Fetching tweets using Twitter handle
                for tweet in list_of_tweets:
                    sentiment = analyze.get_tweet_sentiment(tweet)
                    list_of_tweets_and_sentiments.append((tweet, sentiment))

                context = {
                    'list_of_tweets_and_sentiments': list_of_tweets_and_sentiments,
                    'handle': handle
                }
                # Render emotion_import_result.html located in the 'home' template directory
                return render(request, 'home/sentiment_import_result.html', context)

            else:
                # Handle invalid input (i.e., not a hashtag or Twitter handle)
                return HttpResponse("Invalid handle input. Please enter a valid Twitter handle starting with '@' or a hashtag starting with '#'.")

    else:
        form = Sentiment_Imported_Tweet_analyse_form()

    # Render emotion_import.html located in the 'home' template directory
    return render(request, 'home/sentiment_import.html', {'form': form})

