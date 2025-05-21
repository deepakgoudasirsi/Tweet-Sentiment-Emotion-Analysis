
from django.shortcuts import render, HttpResponse
import pandas as pd
from .forms import Emotion_Typed_Tweet_analyse_form, Emotion_Imported_Tweet_analyse_form
from .emotion_analysis_code import emotion_analysis_code


# Utility function to process tweets and predict emotions
def Import_tweet_emotion(handle):
    list_of_tweets_and_emotions = []

    # Hardcoded dataset path
    dataset_path = "/Users/deepakgouda/Downloads/Twitter_Sentiment_Emotion-Analysis/sentiment_emotion_analysis/text_emotion.csv"

    # Load the dataset
    try:
        df = pd.read_csv(dataset_path)
    except FileNotFoundError:
        print("Dataset not found.")
        return None

    # Validate the dataset structure
    if 'content' not in df.columns or 'sentiment' not in df.columns:
        print("Dataset does not contain required columns.")
        return None

    # Preprocess dataset and handle
    df['content'] = df['content'].str.lower().str.strip()
    df['sentiment'] = df['sentiment'].str.lower().str.strip()
    search_term = handle.lower().replace('#', '').strip()

    # Filter tweets based on content or sentiment
    filtered_tweets = df[(df['content'].str.contains(search_term, na=False, case=False)) |
                         (df['sentiment'].str.contains(search_term, na=False, case=False))]

    # Check for empty results
    if filtered_tweets.empty:
        print(f"No tweets found for the search term: {search_term}")
        return None

    # Analyze filtered tweets
    analyze = emotion_analysis_code()
    for _, row in filtered_tweets.iterrows():
        tweet = row['content']
        emotion = analyze.predict_emotion(tweet)
        list_of_tweets_and_emotions.append((tweet, emotion))

    return {'list_of_tweets': list_of_tweets_and_emotions}


# View for analyzing typed tweets
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
            return render(request, 'home/emotion_type_result.html', context)
    else:
        form = Emotion_Typed_Tweet_analyse_form()

    return render(request, 'home/emotion_type.html', {'form': form})


# View for importing and analyzing tweets based on a handle or hashtag
def emotion_analysis_import(request):
    if request.method == 'POST':
        form = Emotion_Imported_Tweet_analyse_form(request.POST)
        if form.is_valid():
            handle = form.cleaned_data['emotion_imported_tweet']
            tweet_data = Import_tweet_emotion(handle)

            if not tweet_data:
                # Render the 'no tweets found' message
                return HttpResponse("No tweets found for the provided handle or hashtag.")

            context = {
                'list_of_tweets_and_emotions': tweet_data.get('list_of_tweets', []),
                'handle': handle,
            }
            return render(request, 'home/emotion_import_result.html', context)

    else:
        form = Emotion_Imported_Tweet_analyse_form()

    return render(request, 'home/emotion_import.html', {'form': form})
