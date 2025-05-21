from django.shortcuts import render, HttpResponse
from .forms import Emotion_Typed_Tweet_analyse_form, Emotion_Imported_Tweet_analyse_form
from .emotion_analysis_code import emotion_analysis_code
from .tweepy_emotion import Import_tweet_emotion
import pandas as pd

# Assuming you have a CSV file with tweets and emotions
def emotion_analysis(request):
    # Load the dataset (assuming a CSV for this example)
    dataset = pd.read_csv('/Users/deepakgouda/Downloads/Twitter_Sentiment_Emotion-Analysis/sentiment_emotion_analysis/text_emotion.csv')  # Adjust path accordingly

    # Print the columns to check if they match the expected ones
    print(dataset.columns)

    # Extract the relevant columns ('content' for the tweet text and 'sentiment' for the emotion)
    list_of_tweets_and_emotions = dataset[['content', 'sentiment']].values.tolist()

    # Prepare the context to send to the template
    context = {
        'list_of_tweets_and_emotions': list_of_tweets_and_emotions,
    }

    return render(request, 'home/emotion.html', context)


def emotion_analysis_type(request):
    if request.method == 'POST':
        form = Emotion_Typed_Tweet_analyse_form(request.POST)
        if form.is_valid():
            tweet = form.cleaned_data['emotion_typed_tweet']
            emotion = emotion_analysis_code().predict_emotion(tweet)
            context = {
                'tweet': tweet,
                'emotion': emotion
            }
            # Render emotion_type_result.html located in the 'home' template directory
            return render(request, 'home/emotion_type_result.html', context)
    else:
        form = Emotion_Typed_Tweet_analyse_form()

    # Render emotion_type.html located in the 'home' template directory
    return render(request, 'home/emotion_type.html', {'form': form})


def emotion_analysis_import(request):
    if request.method == 'POST':
        form = Emotion_Imported_Tweet_analyse_form(request.POST)
        if form.is_valid():
            handle = form.cleaned_data['emotion_imported_tweet']
            # Use Import_tweet_emotion function to get tweets for the given handle
            tweet_data = Import_tweet_emotion(handle)  # Ensure this function fetches relevant tweets for the handle
            
            if not tweet_data:
                return HttpResponse("No tweets found for the provided handle or hashtag.")

            list_of_tweets_and_emotions = []
            list_of_tweets = tweet_data.get('list_of_tweets', [])

            # Check if the handle starts with a hashtag or '@'
            if handle.startswith('#'):
                # Fetching tweets using hashtag
                for tweet in list_of_tweets:
                    emotion = emotion_analysis_code().predict_emotion(tweet)
                    list_of_tweets_and_emotions.append((tweet, emotion))
                context = {
                    'list_of_tweets_and_emotions': list_of_tweets_and_emotions,
                    'handle': handle
                }
                # Render emotion_import_result_hashtag.html located in the 'home' template directory
                return render(request, 'home/emotion_import_result_hashtag.html', context)

            elif handle.startswith('@'):
                # Fetching tweets using Twitter handle
                for tweet in list_of_tweets:
                    emotion = emotion_analysis_code().predict_emotion(tweet)
                    list_of_tweets_and_emotions.append((tweet, emotion))

                context = {
                    'list_of_tweets_and_emotions': list_of_tweets_and_emotions,
                    'handle': handle
                }
                # Render emotion_import_result.html located in the 'home' template directory
                return render(request, 'home/emotion_import_result.html', context)

            else:
                # Handle invalid input (i.e., not a hashtag or Twitter handle)
                return HttpResponse("Invalid handle input. Please enter a valid Twitter handle starting with '@' or a hashtag starting with '#'.")

    else:
        form = Emotion_Imported_Tweet_analyse_form()

    # Render emotion_import.html located in the 'home' template directory
    return render(request, 'home/emotion_import.html', {'form': form})
