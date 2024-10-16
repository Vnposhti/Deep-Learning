# Import Libraries
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model

# Load Word Index and Model
word_index = imdb.get_word_index()
model = load_model('model_weights.h5')

# Function to preocess User Input Texts
def process_text(user_input):
  words=user_input.lower().split()
  encoded_review = [word_index.get(word,2) + 3 for word in words]
  padded_review = sequence.pad_sequences([encoded_review], maxlen=150)
  return padded_review

# Prediction Function
def predict_sentiment(user_input):
  processed_input = process_text(user_input)
  prediction = model.predict(processed_input)
  sentiment = "Positive" if prediction[0][0] > 0.5 else "Negative"
  return sentiment, prediction[0][0]

# Streamlit
import streamlit as st
st.title('Movie Review Sentiment Analysis')

# Input Text box
user_input = st.text_area('Enter a movie review here.')

#Create a Button
if st.button ('Predict'):
  sentiment, score = predict_sentiment(user_input)
  st.write(f'Sentiment: {sentiment}')
  st.write(f'Prediction Score: {score}')