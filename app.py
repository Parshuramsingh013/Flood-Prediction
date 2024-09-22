import streamlit as st
import numpy as np
import joblib

# Load the trained model
try:
    model = joblib.load('flood_prediction_model.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'flood_prediction_model.pkl' is in the correct directory.")
    st.stop()

# Title
st.title('Flood Probability Prediction')

# Input fields
climate_change = st.number_input('Enter value for Climate Change:')
topography_drainage = st.number_input('Enter value for Topography Drainage:')
dams_quality = st.number_input('Enter value for Dams Quality:')
monsoon_intensity = st.number_input('Enter value for Monsoon Intensity:')

# Predict button
if st.button('Predict Flood Probability'):
    try:
        features = np.array([climate_change, topography_drainage, dams_quality, monsoon_intensity]).reshape(1, -1)
        prediction = model.predict(features)
        st.write(f'Predicted Flood Probability: {prediction[0]:.2f}')
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
