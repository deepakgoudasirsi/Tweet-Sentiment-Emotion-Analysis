from textblob import TextBlob
import pandas as pd
import re

class SentimentAnalyzer:
    def __init__(self):
        self.emotion_keywords = {
            'LOVE': ['love', 'adore', 'loving', 'beloved', 'affection', 'heart', 'care'],
            'HAP': ['happy', 'joy', 'excited', 'wonderful', 'great', 'amazing', 'delighted', 'thrilled', 'fantastic'],
            'SAD': ['sad', 'heartbroken', 'miss', 'crying', 'depressed', 'terrible', 'awful', 'horrible', 'bad', 'poor', 'disappointed'],
            'WOR': ['worried', 'stress', 'anxiety', 'concerned', 'nervous', 'scared', 'fear', 'afraid', 'tension']
        }
        
        # Add strong negative words that should always indicate negative sentiment
        self.strong_negative_words = {
            'kill', 'hate', 'terrible', 'awful', 'horrible', 'bad', 'worst', 'stupid',
            'idiot', 'dumb', 'ugly', 'useless', 'worthless', 'angry', 'mad', 'furious',
            'annoying', 'boring', 'waste', 'wrong', 'fail', 'failure', 'die', 'death',
            'dead', 'sick', 'ill', 'pain', 'hurt', 'suffer', 'suffering', 'cry', 'crying'
        }
    
    def clean_tweet(self, tweet):
        # Remove URLs
        tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
        # Remove user mentions
        tweet = re.sub(r'@\w+', '', tweet)
        # Remove hashtag symbol but keep the text
        tweet = re.sub(r'#', '', tweet)
        return tweet.strip()
    
    def get_sentiment(self, tweet_text):
        cleaned_text = self.clean_tweet(tweet_text.lower())
        words = set(cleaned_text.split())
        
        # Check for strong negative words first
        if any(word in self.strong_negative_words for word in words):
            return 'NEG'
        
        # Use TextBlob for other cases
        analysis = TextBlob(cleaned_text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0.1:
            return 'POS'
        elif polarity < -0.1:
            return 'NEG'
        else:
            return 'NEU'
    
    def get_emotion(self, tweet_text):
        cleaned_text = self.clean_tweet(tweet_text.lower())
        emotion_scores = {emotion: 0 for emotion in self.emotion_keywords.keys()}
        
        # Split text into words for better matching
        words = cleaned_text.split()
        
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                # Check for exact word matches
                if keyword in words:
                    emotion_scores[emotion] += 2  # Give higher weight to exact matches
                # Check for partial matches
                elif keyword in cleaned_text:
                    emotion_scores[emotion] += 1
        
        # If sentiment is negative, give higher weight to negative emotions
        if self.get_sentiment(tweet_text) == 'NEG':
            emotion_scores['SAD'] += 1
            emotion_scores['WOR'] += 1
        
        # Get the emotion with the highest score
        max_score = max(emotion_scores.values())
        if max_score == 0:
            return 'NEU'
        
        return max(emotion_scores.items(), key=lambda x: x[1])[0]
    
    def analyze_tweet(self, tweet_text):
        return {
            'sentiment': self.get_sentiment(tweet_text),
            'emotion': self.get_emotion(tweet_text)
        }
    
    def search_tweets(self, query, dataset_path='tweets_dataset.csv'):
        try:
            df = pd.read_csv(dataset_path)
            # Search in both tweet text and hashtags
            mask = (df['tweet_text'].str.contains(query, case=False, na=False) |
                   df['hashtags'].str.contains(query, case=False, na=False))
            return df[mask]['tweet_text'].tolist()
        except Exception as e:
            print(f"Error reading dataset: {e}")
            return []