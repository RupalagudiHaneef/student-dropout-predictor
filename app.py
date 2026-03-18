import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# Load model, scaler, columns
model = joblib.load('dropout_model.pkl')
scaler = joblib.load('scaler.pkl')
with open('columns.json', 'r') as f:
    columns = json.load(f)

# Page config
st.set_page_config(
    page_title="Student Dropout Predictor",
    layout="centered"
)

# Title
st.title("Student Dropout Risk Predictor")
st.markdown("Enter student details below to predict dropout risk")
st.divider()

# Benchmark info
with st.expander("View Benchmark Guide"):
    st.markdown("""
    **Safe Zone (Based on 4424 Students Data)**
    
    | Factor | Safe Zone | Dropout Average |
    |--------|-----------|----------------|
    | 1st Sem Subjects Approved | 5 or more | Below 5 |
    | 2nd Sem Subjects Approved | 5 or more | Below 5 |
    | 1st Sem Grade | 50+ out of 100 | Below 50 |
    | 2nd Sem Grade | 50+ out of 100 | Below 50 |
    """)

st.divider()

# Student Name & ID
student_name = st.text_input("Student Name")
student_id = st.text_input("Student ID / Roll Number")

st.divider()

# Input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age at Enrollment", 17, 60, 20)
    gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    scholarship = st.selectbox("Scholarship Holder", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    tuition = st.selectbox("Tuition Fees Up to Date", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    debtor = st.selectbox("Debtor", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

with col2:
    sem1_approved = st.number_input("1st Sem Subjects Approved", 0, 10, 5)
    sem1_grade = st.number_input("1st Sem Grade (out of 100)", 0.0, 100.0, 60.0)
    sem2_approved = st.number_input("2nd Sem Subjects Approved", 0, 10, 5)
    sem2_grade = st.number_input("2nd Sem Grade (out of 100)", 0.0, 100.0, 60.0)
    unemployment = st.number_input("Unemployment Rate", 0.0, 50.0, 11.0)

st.divider()

# Convert grades from 100 to 20 scale for model
sem1_grade_converted = sem1_grade / 5
sem2_grade_converted = sem2_grade / 5

# Academic Summary
total_approved = sem1_approved + sem2_approved
avg_grade = (sem1_grade + sem2_grade) / 2

col3, col4 = st.columns(2)
with col3:
    st.metric("Total Subjects Approved", total_approved)
with col4:
    st.metric("Average Grade", f"{avg_grade:.1f} / 100")

st.divider()

# Predict button
if st.button("Predict Dropout Risk", use_container_width=True):

    if not student_name or not student_id:
        st.warning("Please enter Student Name and ID before predicting!")
    else:
        # Create input with all columns set to 0
        input_data = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

        # Fill known inputs
        input_data['Age at enrollment'] = age
        input_data['Gender'] = gender
        input_data['Scholarship holder'] = scholarship
        input_data['Tuition fees up to date'] = tuition
        input_data['Debtor'] = debtor
        input_data['Curricular units 1st sem (approved)'] = sem1_approved
        input_data['Curricular units 1st sem (grade)'] = sem1_grade_converted
        input_data['Curricular units 2nd sem (approved)'] = sem2_approved
        input_data['Curricular units 2nd sem (grade)'] = sem2_grade_converted
        input_data['Unemployment rate'] = unemployment

        # Scale and predict
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]

        # Show student info
        st.markdown(f"### Result for: **{student_name}** (ID: {student_id})")

        # Academic benchmark check
        st.markdown("### Academic Standing")
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            if sem1_approved >= 5:
                st.success(f"Sem 1 Approved: {sem1_approved} (Good)")
            else:
                st.error(f"Sem 1 Approved: {sem1_approved} (Low)")
        with col6:
            if sem2_approved >= 5:
                st.success(f"Sem 2 Approved: {sem2_approved} (Good)")
            else:
                st.error(f"Sem 2 Approved: {sem2_approved} (Low)")
        with col7:
            if sem1_grade >= 50:
                st.success(f"Sem 1 Grade: {sem1_grade} (Good)")
            else:
                st.error(f"Sem 1 Grade: {sem1_grade} (Low)")
        with col8:
            if sem2_grade >= 50:
                st.success(f"Sem 2 Grade: {sem2_grade} (Good)")
            else:
                st.error(f"Sem 2 Grade: {sem2_grade} (Low)")

        st.divider()

        # Show prediction result
        st.markdown("### Prediction Result")
        if prediction == 0:
            st.error(f"DROPOUT RISK — Risk Score: {probability[0]*100:.1f}%")
        elif prediction == 1:
            st.warning(f"ENROLLED — Score: {probability[1]*100:.1f}%")
        else:
            st.success(f"LIKELY TO GRADUATE — Score: {probability[2]*100:.1f}%")

        # Probability breakdown
        st.markdown("### Probability Breakdown")
        prob_df = pd.DataFrame({
            'Status': ['Dropout', 'Enrolled', 'Graduate'],
            'Probability': [f"{probability[0]*100:.1f}%",
                           f"{probability[1]*100:.1f}%",
                           f"{probability[2]*100:.1f}%"]
        })
        st.table(prob_df)

        # Recommended action
        st.markdown("### Recommended Action")
        if prediction == 0:
            st.error("High Risk! Immediate counselor intervention recommended. Check fees status and academic support needs.")
        elif prediction == 1:
            st.warning("Monitor this student. Regular check-ins recommended to prevent dropout.")
        else:
            st.success("On track to graduate! Keep encouraging this student.")