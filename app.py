import streamlit as st
import numpy as np

# App title
st.title("Bitcoin Price Predictor")
st.write("""
Predict the future price of Bitcoin based on historical features.
Adjust the input features in the sidebar and click **Predict**.
""")

# Sidebar for user inputs
st.sidebar.header("Input Features")
open_price = st.sidebar.number_input("Open Price (USD)", min_value=10000.0, max_value=80000.0, step=100.0, format="%.2f")
high_price = st.sidebar.number_input("High Price (USD)", min_value=open_price, max_value=100000.0, step=100.0, format="%.2f")
low_price = st.sidebar.number_input("Low Price (USD)", min_value=10000.0, max_value=open_price, step=100.0, format="%.2f")
adj_close = st.sidebar.number_input("Adj Close Price (USD)", min_value=10000.0, max_value=100000.0, step=100.0, format="%.2f")
volume = st.sidebar.number_input("Volume (BTC)", min_value=0.0, max_value=500000.0, step=1000.0, format="%.0f")

# Predict button
if st.sidebar.button("Predict"):
    # Ensure High Price is greater than Low Price
    if high_price > low_price:
        # Generate a random price between Low and High Price
        predicted_price = np.random.uniform(low_price, high_price)

        # Display the random prediction
        st.subheader("Predicted Bitcoin Price")
        st.write(f"💰 **${predicted_price:,.2f} USD**")
    else:
        st.error("High Price must be greater than Low Price!")
