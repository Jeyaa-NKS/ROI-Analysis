

import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved modelimport base64  #to open .gif files in streamlit app


@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No": 1, "Yes": 2}
    for key, value in feature_dict.items():
        if val == key:
            return value

def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value

import base64  # to open .gif files in Streamlit app

def set_background(style):
    # Adding custom CSS
    style = f"""
    <style>
    .reportview-container {{
        background: url(data:image/jpeg;base64,{base64.b64encode(style).decode()});
        background-size: cover;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

# Load the background image
background_image = open("BA2.jpg", "rb").read()
set_background(background_image)



#if app_mode == 'Home':
    # Your Home page content
st.title("Welcome to the Profitability Unleashed!!")
st.write("Step into a world where possibilities are endless, and your dreams become reality. With our innovative solutions and unwavering commitment, we're here to help you reach new heights and unlock your full potential. Join us on this extraordinary journey, where every click, every choice, and every moment counts. Your adventure begins here – where the future meets today, and success is more than just a goal; it's a way of life. Embrace the extraordinary, and together, let's make the remarkable happen")


#elif app_mode == 'Prediction':
 #   # Your Prediction page content
  #  st.write("This is the Prediction page.")
#
    # You can call your functions here based on the selected page
    # For instance:
 #   value = get_fvalue("Yes")  # Example usage of the get_fvalue function
  #  st.write("Value for 'Yes' in feature_dict:", value)
