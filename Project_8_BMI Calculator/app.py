import streamlit as st
import pandas as pd

st.title("BMI Calculator")
height = st.slider("Enter Your Height (in cm) : ", 100,250,175)
weight = st.slider("Enter Your Weight (in kg) : ", 40,200,70)

bmi = weight / ((height / 100) ** 2)
rounded_bmi = round(bmi, 2)  # Round BMI to 2 decimal places
st.success(f"Your BMI is: {rounded_bmi}")

if rounded_bmi < 18.5:
    st.warning("You are underweight !!!")
elif rounded_bmi <= 24 and rounded_bmi >= 18.5:
    st.success("You are Normal")
elif rounded_bmi >24.5 and rounded_bmi <= 30:
    st.warning("You are Overweight !!!") 
elif rounded_bmi > 30:
    st.warning("You are Obesity !!!") 


st.write("### BMI Catagories ###")
st.text("--- Underweight : BMI Less Than 18.5 ---")
st.write("--- Normal : BMI between 18.5 to 24.5 ---")
st.write("--- OverWeight : BMI between 24.5 to 30 ---")
st.write("--- Obesity : BMI Greater Than 30 ---")