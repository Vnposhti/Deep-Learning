# Next Word Prediction Using GRU

## Overview
This repository contains a Recurrent Neural Network (RNN) model, specifically using a Gated Recurrent Unit (GRU) architecture, to predict the next word in a sequence of text. The model is trained on the Hamlet dataset, sourced from Project Gutenberg, which contains Shakespeare's Hamlet.

The GRU model is designed to learn the patterns and relationships between words, enabling it to generate accurate predictions of the next word based on the preceding context. GRUs, like LSTMs, are well-suited for sequential data tasks, but with a simpler architecture that often leads to faster training while maintaining strong performance.

The model preprocesses the text by tokenizing words and generating sequences where each input is a series of preceding words and the target output is the next word. The dataset is then split into training and validation sets to assess model performance.

Once trained, the model can be used for text generation in Shakespearean style, predicting the next word in a sentence or phrase. The GRU architecture can be applied in various natural language processing (NLP) tasks like text generation, creative writing aids, and language modeling.

This project demonstrates how GRU networks can be effectively used in natural language processing, especially for next-word prediction in classical literature, offering a balance of performance and computational efficiency.

## Live Demo
You can access the live Streamlit application at the following link:
[GRU NEXT WORD PREDICTION](https://gru-word-prediction-023.streamlit.app/)

## Main Components
The main components of this repository include:
- **`gru_word_prediction.ipynb`**: Jupyter Notebook implementing the LSTM model for next word prediction.
- **`app.py`**: A user-friendly Streamlit web application to interact with the models.

## How to Use
1. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the web application:
    ```bash
    streamlit run app.py
    ```

3. Explore the notebooks for detailed analysis and model building.

---

### Feel free to contribute to this project by submitting issues or pull requests!