import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os
# Load model
rfr = pickle.load(open('rfr.pkl', 'rb'))

def pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp):
    features = np.array([[Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp]])
    prediction = rfr.predict(features)
    return prediction[0]

# Streamlit App
st.title("Calories Burn Prediction")

# Input Fields (Users can enter values instead of selecting)
Gender = st.radio("Gender", [0, 1])  # Assuming 0 = Female, 1 = Male
Age = st.number_input("Enter Age", min_value=10, max_value=100, value=25)
Height = st.number_input("Enter Height (cm)", min_value=100, max_value=250, value=170)
Weight = st.number_input("Enter Weight (kg)", min_value=30, max_value=200, value=70)
Duration = st.number_input("Exercise Duration (minutes)", min_value=1, max_value=300, value=30)
Heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=100)
Body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0, step=0.1)

if st.button('Predict'):
    result = pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp)
    st.success(f"You have burned approximately {result:.2f} calories.")
st.write("Current Working Directory:", os.getcwd())

# Check if model file exists before loading
model_path = os.path.join(os.getcwd(), "rfr.pkl")

if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        rfr = pickle.load(f)
else:
    st.error(f"Model file 'rfr.pkl' not found at {model_path}. Ensure it is correctly uploaded.")