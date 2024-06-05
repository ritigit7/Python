import streamlit as st
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Custom CSS for better mobile look
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .main-title {
        text-align: center;
        font-size: 2rem;
        color: #4CAF50;
    }
    .description {
        text-align: center;
        font-size: 1rem;
        color: #333;
    }
    .input-box {
        text-align: center;
    }
    .input-box input {
        width: 90%;
        padding: 10px;
        margin: 10px 0;
        border-radius: 10px;
        border: 1px solid #ccc;
    }
    .predict-button {
        text-align: center;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-size: 1rem;
    }
    .predict-button:hover {
        background-color: #45a049;
    }
    .predicted-word {
        text-align: center;
        font-size: 1.5rem;
        color: #333;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="main-title">Next Word Predictor</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="description">
        This app predicts the next word in a sentence using a pre-trained LSTM model. 
        Enter a sentence to see the next predicted word.
    </div>
""", unsafe_allow_html=True)

# Try loading the model and catch exceptions
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model('D:/python programs/All/.venv/Include/Next Word Predictor/App_Model.keras')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# Load the tokenizer
@st.cache_resource
def load_tokenizer():
    try:
        with open("D:/python programs/All/.venv/Include//Next Word Predictor/token.pkl", 'rb') as f:
            token = pickle.load(f)
        return token
    except Exception as e:
        st.error(f"Error loading tokenizer: {e}")
        return None

token = load_tokenizer()

# Function to predict the next word
def predict_next_word(text):
    try:
        xt = token.texts_to_sequences([text])[0]
        sq = pad_sequences([xt], maxlen=250, padding='pre')
        n = np.array(sq[0]).reshape(1, len(sq[0]), 1)
        y = model.predict(n)

        max_index = np.argmax(y)
        word_index = token.word_index

        def get_key_from_value(d, value):
            for key, val in d.items():
                if val == value:
                    return key
            return None

        next_word = get_key_from_value(word_index, max_index)
        return next_word
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None

# User input
st.markdown('<div class="input-box"><label>Enter a sentence to predict the next word:</label></div>', unsafe_allow_html=True)
user_input = st.text_input("", "", key="input")

if st.button("Predict Next Word", key="predict"):
    if user_input:
        predicted_word = predict_next_word(user_input)
        if predicted_word:
            st.markdown(f'<div class="predicted-word">Predicted next word: <strong>{predicted_word}</strong></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="predicted-word">Unable to predict the next word.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="predicted-word">Please enter a sentence to predict the next word.</div>', unsafe_allow_html=True)
