# IMDB Movie Review Sentiment Analysis Using SimpleRNN

## Overview
This repository contains a Recurrent Neural Network (RNN) model, specifically using a SimpleRNN architecture, to perform sentiment analysis on IMDB movie reviews. The model predicts whether a given movie review expresses positive or negative sentiment based on the text data. The IMDB dataset, containing 50,000 movie reviews, is used to train and evaluate the model.

## Live Demo
You can access the live Streamlit application at the following link:

[Movie Sentiment Analysis APP](https://imdb-sentiment-analysis-023.streamlit.app/)

## Dataset
[IMDB Movie Review](https://ai.stanford.edu/%7Eamaas/data/sentiment/)


## Main Components
The main components of this repository include:

- **`IMDB_Sentiment_Analysis.ipynb`**: Jupyter Notebook implementing the SimpleRNN model for Sentiment Analysis.
- **`Imdb_review_prediction.ipynb`**: Script to make predictions using the trained models.
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