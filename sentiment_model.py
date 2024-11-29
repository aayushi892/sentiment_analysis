import pandas as pd
from transformers import pipeline
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download NLTK data
nltk.download('vader_lexicon')

# Initialize Hugging Face's sentiment pipeline
huggingface_pipeline = pipeline('sentiment-analysis')

# Initialize NLTK's Vader Sentiment Analyzer
vader_analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_huggingface(text):
    """Analyze sentiment using Hugging Face's Transformer model."""
    result = huggingface_pipeline(text)[0]
    return result['label'], result['score']

def analyze_sentiment_vader(text):
    """Analyze sentiment using NLTK's Vader Sentiment Analyzer."""
    scores = vader_analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return 'Positive', scores['compound']
    elif scores['compound'] <= -0.05:
        return 'Negative', scores['compound']
    else:
        return 'Neutral', scores['compound']
