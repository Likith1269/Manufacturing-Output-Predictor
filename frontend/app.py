import streamlit as st
import requests

st.title("Manufacturing Output Predictor")

Injection_Temperature = st.number_input("Injection Temperature")
Injection_Pressure = st.number_input("Injection Pressure")
Cycle_Time = st.number_input("Cycle Time")
Cooling_Time = st.number_input("Cooling Time")
Machine_Age = st.number_input("Machine Age")

if st.button("Predict"):
    data = {
        "Injection_Temperature": Injection_Temperature,
        "Injection_Pressure": Injection_Pressure,
        "Cycle_Time": Cycle_Time,
        "Cooling_Time": Cooling_Time,
        "Machine_Age": Machine_Age
    }

    try:
        response = requests.post(
            "https://manufacturing-output-predictor.onrender.com/predict",
            json=data
        )

        result = response.json()
        st.success(f"Predicted Parts Per Hour: {result['Predicted_Parts_Per_Hour']}")

    except:
        st.error("Backend is not responding")
