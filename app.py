import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("insurance_model.pkl", "rb"))

st.title("🏥 Insurance Charges Prediction")

st.write("Enter your details below:")

# Numeric Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=24.5)
children = st.number_input("Children", min_value=0, max_value=10, value=2)

# Categorical Inputs
sex = st.selectbox("Sex", ["Female", "Male"])
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox(
    "Region",
    ["Northeast", "Northwest", "Southeast", "Southwest"]
)

# Prediction
if st.button("Predict Charges"):

    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'children': [children],
        'sex_male': [1 if sex == "Male" else 0],
        'smoker_yes': [1 if smoker == "Yes" else 0],
        'region_northwest': [1 if region == "Northwest" else 0],
        'region_southeast': [1 if region == "Southeast" else 0],
        'region_southwest': [1 if region == "Southwest" else 0]
    })

    prediction = model.predict(input_data)

    st.success(f"💰 Estimated Insurance Charges: ${prediction[0]:,.2f}")