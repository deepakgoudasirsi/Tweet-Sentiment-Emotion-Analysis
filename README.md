# Tweet-Sentiment-Emotion-Analysis

This project analyzes the sentiment and emotions of tweets using machine learning and natural language processing techniques. It supports analyzing typed tweets and fetching tweets by Twitter handles or hashtags.

---

## **Features**

1. **Analyze Typed Tweets**:
    
    Users can manually type a tweet and analyze its sentiment (e.g., Positive, Negative, Neutral).
    
2. **Analyze Imported Tweets**:
    
    Fetch tweets using Twitter handles (`@username`) or hashtags (`#hashtag`) and analyze their sentiment.
    
3. **CSV Dataset Analysis**:
    
    Load a dataset of tweets and display their associated sentiments and emotions.
    

---

## **Technologies Used**

- **Backend**: Django (Python)
- **Data Processing**: Pandas
- **Twitter API Integration**: Tweepy
- **Frontend**: HTML, CSS (Django Templates)
- **Machine Learning**: Custom sentiment analysis code

---

##  **Project Structure**

```
Tweet-Sentiment-Emotion-Analysis/
│
├── SENTIMENT_Emotion-Analysis/   # Main Django project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── emotion/                      # Django app directory (assuming it was named 'emotion')
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── migrations/                   # Django migrations directory
│   └── __init__.py
│
├── static/                       # Static files (CSS, JS, images)
│   └── css/
│       └── styles.css
│
├── templates/home/               # Template files for the 'home' app
│   ├── sentiment.html
│   ├── sentiment_import.html
│   ├── sentiment_import_result.html
│   ├── sentiment_import_result_hashtag.html
│   ├── sentiment_type.html
│   └── sentiment_type_result.html
│
├── sentiment_analysis_code.py    # Contains code for analyzing sentiment
├── tweepy_sentiment.py           # Handles importing tweets using Tweepy
│
├── text_emotion.csv              # CSV dataset with tweets and emotions
├── db.sqlite3                    # SQLite database file
├── debug.log                     # Log file for debugging
├── manage.py                     # Django management script
│
└── .idea/                        # IDE configuration (e.g., for PyCharm)

```

---

## 📦 **Dataset**

The project uses a CSV dataset containing tweets and their associated sentiments.

- **Sample CSV Path**: `/path/to/your/text_emotion.csv`
- **Expected Columns**:
    - `content`: The tweet text
    - `sentiment`: The sentiment label (e.g., Happy, Sad, Angry)

---

## ⚙️ **Setup Instructions**

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Tweet-Sentiment-Emotion-Analysis.git
cd Tweet-Sentiment-Emotion-Analysis

```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```


### 4. Run Migrations

```bash
python manage.py migrate

```

### 5. Run the Development Server

```bash
python manage.py runserver

```

Open your browser and navigate to **`http://127.0.0.1:8000`**.
