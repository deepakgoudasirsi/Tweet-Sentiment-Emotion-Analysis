from django.shortcuts import render, HttpResponse
import pandas as pd
from .forms import Sentiment_Typed_Tweet_analyse_form, Sentiment_Imported_Tweet_analyse_form
from .sentiment_analysis_code import sentiment_analysis_code


# Utility function to process tweets and predict emotions
def Import_tweet_sentiment(handle):
    list_of_tweets_and_sentiments = []

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
    analyze = sentiment_analysis_code()
    for _, row in filtered_tweets.iterrows():
        tweet = row['content']
        sentiment = analyze.get_tweet_sentiment(tweet)
        list_of_tweets_and_sentiments.append((tweet, sentiment))

    return {'list_of_tweets': list_of_tweets_and_sentiments}


# View for analyzing typed tweets
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
            return render(request, 'home/sentiment_type_result.html', context)
    else:
        form = Sentiment_Typed_Tweet_analyse_form()

    return render(request, 'home/sentiment_type.html', {'form': form})


# View for importing and analyzing tweets based on a handle or hashtag
def sentiment_analysis_import(request):
    if request.method == 'POST':
        form = Sentiment_Imported_Tweet_analyse_form(request.POST)
        if form.is_valid():
            handle = form.cleaned_data['sentiment_imported_tweet']
            tweet_data = Import_tweet_sentiment(handle)

            if not tweet_data:
                # Render the 'no tweets found' message
                return HttpResponse("No tweets found for the provided handle or hashtag.")

            context = {
                'list_of_tweets_and_sentiments': tweet_data.get('list_of_tweets', []),
                'handle': handle,
            }
            return render(request, 'home/sentiment_import_result.html', context)

    else:
        form = Sentiment_Imported_Tweet_analyse_form()

    return render(request, 'home/sentiment_import.html', {'form': form})
