import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
@st.cache(allow_output_mutation=True)
def load_trained_model():
    return load_model('spending_limit_prediction_model.h5')

# Load new data for prediction
@st.cache
def load_new_data():
    new_data = pd.read_csv('/content/cust.csv')  # Replace with the correct path
    return new_data

# Function for predicting spending limit
def predict_spending_limit(model, new_data):
    X_new = new_data[['Earning', 'Earning Potential']].values
    predicted_spending_limit = model.predict(X_new)
    prediction_data = new_data[['Customer Name', 'Earning', 'Earning Potential']].copy()
    prediction_data['Predicted Spending Limit'] = predicted_spending_limit
    return prediction_data

# Streamlit app
st.title('Spending Limit Prediction')

# Load the model and new data
loaded_model = load_trained_model()
new_data = load_new_data()

# Display new data
st.subheader('New Data for Prediction')
st.write(new_data.head())

# Predict spending limit
predicted_data = predict_spending_limit(loaded_model, new_data)

# Display predicted spending limit
st.subheader('Predicted Spending Limits for New Data')
st.write(predicted_data.head())
