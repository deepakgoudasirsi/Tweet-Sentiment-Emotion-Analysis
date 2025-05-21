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

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tweet-sentiment-analysis.git
   cd tweet-sentiment-analysis
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django textblob nltk pandas
   ```

4. **Download NLTK data**
   ```bash
   python3 -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
   ```

5. **Apply database migrations**
   ```bash
   python3 manage.py migrate
   ```

6. **Run the development server**
   ```bash
   python3 manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

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

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- TextBlob for sentiment analysis
- NLTK for natural language processing
- Django for the web framework
- Tailwind CSS for the UI components
