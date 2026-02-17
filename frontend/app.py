import streamlit as st
import requests

st.set_page_config(page_title="Manufacturing Predictor", layout="centered")

st.title("🏭 Manufacturing Output Predictor")

st.write("Enter values and click Predict")

# Inputs
Injection_Temperature = st.number_input("Injection Temperature", value=0.0)
Injection_Pressure = st.number_input("Injection Pressure", value=0.0)
Cycle_Time = st.number_input("Cycle Time", value=0.0)
Cooling_Time = st.number_input("Cooling Time", value=0.0)
Machine_Age = st.number_input("Machine Age", value=0.0)

if st.button("Predict"):
    data = {
        "Injection_Temperature": Injection_Temperature,
        "Injection_Pressure": Injection_Pressure,
        "Cycle_Time": Cycle_Time,
        "Cooling_Time": Cooling_Time,
        "Machine_Age": Machine_Age
    }

    try:
response = requests.post("https://manufacturing-output-predictor.onrender.com/predict", json=data)
        result = response.json()
        st.success(f"Predicted Parts Per Hour: {result['Predicted_Parts_Per_Hour']}")
    except:
        st.error("Backend not running")
