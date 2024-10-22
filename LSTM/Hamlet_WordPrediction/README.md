# Next Word Prediction Using LSTM

## Overview
This repository contains a Recurrent Neural Network (RNN) model, specifically using a Long Short-Term Memory (LSTM) architecture, to predict the next word in a sequence of text. The model is trained on the Hamlet dataset, which is sourced from Project Gutenberg, and contains Shakespeare's Hamlet text.

The LSTM model is designed to learn the sequential patterns and relationships between words in the dataset, enabling it to generate predictions of the next word based on the preceding context. By leveraging LSTM’s ability to retain long-term dependencies in sequential data, this model effectively captures the complexities of natural language, particularly in the literary style of Shakespeare.

The model preprocesses the text data by tokenizing the words and creating sequences of input data, where each sequence represents a fixed number of preceding words and the corresponding next word. The dataset is then split into training and validation sets to evaluate the model's performance.

Once trained, the model can be used to generate Shakespearean-style text by predicting the next word in a sentence or phrase. It can also serve as a foundational model for tasks such as text generation, language modeling, or enhancing creativity in literary text completion.

This project demonstrates the application of LSTM models in natural language processing (NLP), providing a stepping stone for further exploration into text generation and language understanding using classical literature.

## Live Demo
You can access the live Streamlit application at the following link:
[LSTM NEXT WORD PREDICTION](https://lstm-word-prediction-023.streamlit.app/)

## Main Components
The main components of this repository include:
- **`lstm_word_prediction.ipynb`**: Jupyter Notebook implementing the LSTM model for next word prediction.
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