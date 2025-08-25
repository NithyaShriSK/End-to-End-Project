import streamlit as st
import pickle
import numpy as np



model , scaler = pickle.load(open('model.sav', 'rb'))


st.title("Salary Prediction App")

st.write("Enter the details below to predict the salary.")


Education = st.number_input("Education:", min_value=20, max_value=1000, value=100)
Experience = st.number_input("Experience:", min_value=1, max_value=10, value=2)
Location = st.number_input("Location:", min_value=1, max_value=3, value=1)
Job_Title = st.number_input("Job Title:", min_value=1, max_value=20, value=5)
Age = st.number_input("Age:", min_value=1, max_value=70, value=25)
Gender = st.number_input("Gender:",min_value=1,max_value=3,value=1)
features = np.array([[Education,Experience,Location,Job_Title,Age,Gender]])

features_scaled = scaler.transform(features)

if st.button("Predict Price"):
    prediction = model.predict(features_scaled)
    st.success(f"Estimated Price: {prediction[0]:,.2f}")
    
    