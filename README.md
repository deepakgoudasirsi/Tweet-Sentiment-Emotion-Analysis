# Tweet Sentiment & Emotion Analysis

A powerful web application that analyzes tweets for sentiment and emotions, helping users understand the emotional context of social media content.

## Overview

This project provides real-time sentiment and emotion analysis for tweets. It can analyze any text input for sentiment (Positive, Negative, Neutral) and detect emotions (Love, Happiness, Sadness, Worry). The application also includes a dataset-based tweet search feature.

## Tech Stack

- **Backend:**
  - Python 3.x
  - Django (Web Framework)
  - TextBlob (Natural Language Processing)
  - NLTK (Text Processing)
  - Pandas (Data Handling)

- **Frontend:**
  - HTML5
  - Tailwind CSS (Styling)
  - jQuery (AJAX & DOM Manipulation)
  - JavaScript

- **Database:**
  - SQLite (Development)
  - CSV (Tweet Dataset)

## Features

1. **Sentiment Analysis**
   - Classifies text as Positive, Negative, or Neutral
   - Uses TextBlob for accurate sentiment detection
   - Real-time analysis without page reload

2. **Emotion Detection**
   - Identifies four main emotions: Love, Happiness, Sadness, Worry
   - Keyword-based analysis with custom scoring
   - Context-aware emotion detection

3. **Tweet Search**
   - Search through dataset using keywords or hashtags
   - Real-time search results
   - Case-insensitive matching

4. **Modern UI**
   - Responsive design using Tailwind CSS
   - Clean and intuitive interface
   - Real-time updates with AJAX

## 🚀 Getting Started

 **Clone the repository**
   ```bash
   git clone https://github.com/deepakgoudasirsi/tweet-sentiment-analysis.git
   cd tweet-sentiment-analysis
   ```

## Project Structure

```
tweet-sentiment-analysis/
├── sentiment_app/
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   └── templates/
│       └── sentiment_app/
│           └── home.html
├── tweet_analysis/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tweets_dataset.csv
├── manage.py
└── README.md
```

---

## Contact

* **Deepak Gouda**
  [GitHub @deepakgoudasirsi](https://github.com/deepakgoudasirsi)
  [LinkedIn: Deepak Gouda](https://linkedin.com/in/deepakgoudasirsi)
