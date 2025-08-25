import streamlit as st
import pickle
import numpy as np



model , scaler = pickle.load(open('model.sav', 'rb'))


st.title("Salary Prediction App")

st.write("Enter the details below to predict the salary.")


import streamlit as st
import numpy as np

# Dropdown for Education Level (example categories)
Education = st.selectbox(
    "Education Level:",
    options=["High School", "Bachelor's", "Master's", "PhD"],
    index=1
)

# Numeric input for Experience
Experience = st.number_input("Experience (Years):", min_value=0, max_value=40, value=2)

# Dropdown for Location
Location = st.selectbox(
    "Location:",
    options=["Rural", "Suburban", "Urban"],
    index=0
)

# Dropdown for Job Title
Job_Title = st.selectbox(
    "Job Title:",
    options=["Engineer", "Director", "Manager", "Analyst"],
    index=0
)

# Numeric input for Age
Age = st.slider("Age:", min_value=5, max_value=70, value=25)

# Dropdown for Gender
Gender = st.radio(
    "Gender:",
    options=["Male", "Female"],
    index=0
)

# --- Encoding categorical values ---
edu_map = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
loc_map = {"Rural": 1, "Suburban": 2, "Urban": 3}
job_map = {"Engineer": 1, "Director": 2, "Manager": 4, "Analyst": 2}
gender_map = {"Male": 1, "Female": 0}

features = np.array([[
    edu_map[Education],
    Experience,
    loc_map[Location],
    job_map[Job_Title],
    Age,
    gender_map[Gender]
]])


features_scaled = scaler.transform(features)

if st.button("Predict Price"):
    prediction = model.predict(features_scaled)
    st.success(f"Estimated Price: {prediction[0]:,.2f}")
    
    