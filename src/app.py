from pickle import load
import streamlit as st
from sklearn.preprocessing import StandardScaler
import joblib
import os

model = load(open("/workspaces/Isa-Streamlit/models/Reg-Lin_5vars.sav", "rb"))
scaler = joblib.load('/workspaces/Isa-Streamlit/models/scaler_model.joblib')

st.title("Calculate your assurance cost")

age = st.slider("Age", min_value = 18.0, max_value = 100.0, step = 1.0)
smoke = st.selectbox("Smoke?", options=["yes","no"])
sex = st.selectbox("Sex", options=["male","female"])
reg = st.selectbox("Your Region", options=["southwest","southeast","northwest","northeast"])
kg = st.slider("Weight (kg)", min_value = 20.0, max_value = 200.0, step = 1.0)
cm = st.slider("Height (cm)", min_value = 80.0, max_value = 220.0, step = 1.0)

smoke_n= 0 if smoke == 'yes' else 1
sex_n= 0 if sex== 'female' else 1

if reg == 'southwest':
    reg_n = 0
elif reg == 'southeast':
    reg_n = 1
elif reg == 'northwest':
    reg_n = 2
else:
    reg_n = 3

bmi=kg/((cm/100)**2)

        
data_for_norm=[[age, bmi,0, sex_n,smoke_n,reg_n]]
data_norm = scaler.transform(data_for_norm)
data = [[data_norm[0][4], data_norm[0][0], data_norm[0][1], data_norm[0][3],data_norm[0][5]]]

if st.button("Predict"):
    prediction = str(round(model.predict(data)[0]))
    
    st.write("El precio de su seguro será de:", prediction)