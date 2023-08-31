import streamlit as st
import pandas as pd
import pickle

# Load the random forest classifier model
model = pickle.load(open("/Users/samhan_6/Downloads/DeployModel/final_model.pkl", "rb"))

# Create a function to make predictions
def predict(gravity, ph, osmo, cond, urea, calc):
    features = pd.DataFrame({
        "gravity": gravity,
        "ph": ph,
        "osmo": osmo,
        "cond": cond,
        "urea": urea,
        "calc": calc
    }, index=[0])
    prediction = model.predict(features)
    return prediction

# Create a Streamlit app
st.title("Kidney Stone Prediction")

# Input fields for the features
gravity = st.number_input("Gravity: ")
ph = st.number_input("pH: ")
osmo = st.number_input("Osmolarity: ")
cond = st.number_input("Conductivity: ")
urea = st.number_input("Urea: ")
calc = st.number_input("Calcium: ")

result = ""
if st.button("Predict"):
    result = predict(gravity, ph, osmo, cond, urea, calc)
    st.success('The output is {}'.format(result))
