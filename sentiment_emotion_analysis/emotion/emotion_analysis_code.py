import re
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import itertools
import nltk
import numpy as np

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

class emotion_analysis_code:
    lem = WordNetLemmatizer()

    def cleaning(self, text):
        txt = str(text)
        txt = re.sub(r"http\S+", "", txt)  # Remove URLs
        if len(txt) == 0:
            return 'no text'
        else:
            txt = txt.split()
            index = [j for j in range(len(txt)) if txt[j][0] == '@']  # Remove mentions
            txt = np.delete(txt, index) if len(index) > 0 else txt
            if len(txt) == 0:
                return 'no text'
            else:
                words = ' '.join(txt)
                txt = re.sub(r'[^\w]', ' ', words)  # Remove special characters
                if len(txt) == 0:
                    return 'no text'
                else:
                    txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))  # Remove repeated characters
                    txt = txt.replace("'", "")
                    txt = nltk.tokenize.word_tokenize(txt)
                    txt = [self.lem.lemmatize(word, "v") for word in txt]
                    return txt if len(txt) > 0 else 'no text'

    def predict_emotion(self, tweet):
        """
        Predict the emotion based on keywords or simple sentiment analysis.
        """
        # Clean the tweet
        tweet_cleaned = ' '.join(self.cleaning(tweet))
        
        # Analyze sentiment using TextBlob
        analysis = TextBlob(tweet_cleaned)
        polarity = analysis.sentiment.polarity
        
        # Map sentiment polarity to an emotion
        if polarity > 0.5:
            return 'Happiness'
        elif polarity > 0:
            return 'Love'
        elif polarity == 0:
            return 'Neutral'
        elif polarity < -0.5:
            return 'Sadness'
        else:
            return 'Worry'

# Example usage
if __name__ == "__main__":
    analyzer = EmotionAnalysis()
    tweet = "@user I can't believe it's raining again! So much for my plans. #worried"
    emotion = analyzer.predict_emotion(tweet)
    print(f"The predicted emotion is: {emotion}")
