# Import Libraries
import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load Model
model=load_model('gru_model.h5')

#Load Tokenizer
with open ('gru_tokenizer.pickle','rb') as handle:
    tokenizer=pickle.load(handle)

# Prediction
def predict_next_word(model,tokenizer,data,max_length):
    token_list = tokenizer.texts_to_sequences([data])[0]
    if len(token_list) >= max_length:
        token_list = token_list[-(max_length-1):] # Ensure the sequnce length matches the max length
    token_list = pad_sequences([token_list], maxlen=max_length-1, padding='pre')
    prediction = model.predict(token_list, verbose=0)
    predicted_index = np.argmax(prediction, axis=1)
    for word,index in tokenizer.word_index.items():
        if index == predicted_index:
            return word
    return None

# Steramlit
st.title('Next Word Prediction with GRU')
input_text=st.text_input('Enter the sequence of words here')
if st.button("Predict"):
    max_length=model.input_shape[1] + 1
    next_word=predict_next_word(model,tokenizer,input_text,max_length)
    st.write(f'Next Word: {next_word}')