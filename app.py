# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wapxPtHMKeSIBiV8FmCOL5DPglgwF3HK
"""

import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title
st.title("Bitcoin Price Movement Predictor")
st.write("Predict whether the Bitcoin closing price will go UP or DOWN based on input data.")

# Sidebar for user inputs
st.sidebar.header("Input Features")
open_price = st.sidebar.number_input("Open Price", min_value=0.0, step=0.01, format="%.2f")
high_price = st.sidebar.number_input("High Price", min_value=0.0, step=0.01, format="%.2f")
low_price = st.sidebar.number_input("Low Price", min_value=0.0, step=0.01, format="%.2f")
volume = st.sidebar.number_input("Volume", min_value=0.0, step=1.0, format="%.2f")

# Predict button
if st.sidebar.button("Predict"):
    # Prepare input data
    input_data = np.array([[open_price, high_price, low_price, volume]])

    # Make prediction
    prediction = model.predict(input_data)

    # Display prediction
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.write("📈 **The closing price will go UP!**")
    else:
        st.write("📉 **The closing price will go DOWN!**")