import streamlit as st
from sentiment_model import analyze_sentiment_huggingface, analyze_sentiment_vader

st.title("Real-Time Sentiment Analysis App")
st.write("Analyze user sentiments from text input using NLP models.")

# Text input from user
user_input = st.text_area("Enter text to analyze sentiment:")

# Hugging Face sentiment analysis
if st.button("Analyze Sentiment (Hugging Face)"):
    label, score = analyze_sentiment_huggingface(user_input)
    st.write(f"Sentiment: {label}")
    st.write(f"Confidence Score: {score:.2f}")

# Vader sentiment analysis
if st.button("Analyze Sentiment (Vader)"):
    label, score = analyze_sentiment_vader(user_input)
    st.write(f"Sentiment: {label}")
    st.write(f"Compound Score: {score:.2f}")
