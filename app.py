import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# App title
st.title("🩺 Diabetes Risk Score Predictor")
st.markdown("Enter your health parameters below:")

# Input fields
weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=70.0)
height = st.number_input("Height (cm)", min_value=100.0, max_value=220.0, value=170.0)
blood_glucose = st.number_input("Blood Glucose Level", min_value=50.0, max_value=300.0, value=110.0)
physical_activity = st.number_input("Physical Activity (mins/day)", min_value=0.0, max_value=300.0, value=30.0)
diet = st.selectbox("Healthy Diet?", [0, 1])
medication_adherence = st.selectbox("Medication Adherence (0=Poor, 1=Good, 2=Excellent)", [0, 1, 2])
stress_level = st.selectbox("High Stress Level?", [0, 1])
sleep_hours = st.number_input("Sleep Duration (hours)", min_value=0.0, max_value=24.0, value=7.0)
hydration_level = st.selectbox("Hydration Adequate?", [0, 1])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=24.0)

# Prediction
if st.button("Predict Risk Score"):
    input_df = pd.DataFrame([{
        "weight": weight,
        "height": height,
        "blood_glucose": blood_glucose,
        "physical_activity": physical_activity,
        "diet": diet,
        "medication_adherence": medication_adherence,
        "stress_level": stress_level,
        "sleep_hours": sleep_hours,
        "hydration_level": hydration_level,
        "bmi": bmi
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Diabetes Risk Score: **{prediction:.2f}**")
