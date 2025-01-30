import joblib
import streamlit as st 
import numpy as np 
 
#load model and scaler
model = joblib.load("./model/model.joblib")

st.markdown( """ <style> .title { text-align: center; } </style> """, unsafe_allow_html=True )

st.markdown('<h1 class="title">Prediction of student status</h1>', unsafe_allow_html=True)

marital_mapping = {
    'single': 1,
    'married': 2,
    'widower': 3,
    'divorced': 4,
    'facto union': 5,
    'legally separated': 6
}

yes_no_mapping = {
    'no': 0,
    'yes': 1
}

attendance_mapping = {
    'daytime': 1,
    'evening': 0
}

col1, col2 = st.columns(2)
with col1:
    marital_status = st.selectbox("Marital Status?", list(marital_mapping.keys()))
with col2:
    debtor = st.selectbox("Debtor?", list(yes_no_mapping.keys()))

col1, col2, col3 = st.columns(3)
with col1:
    tuition = st.selectbox("Tuition Fees Up to Date?", list(yes_no_mapping.keys()))
with col2:
    scholarship = st.selectbox("Scholarship Holder?", list(yes_no_mapping.keys()))
with col3:
    attend = st.selectbox("Attendance?", list(attendance_mapping.keys()))

col1, col2 = st.columns(2)
with col1:
    curricular_1st_sem_approved = st.number_input("Curricular First Semester Approved", min_value=0, max_value=30, step=1)
with col2:
    curricular_1st_sem_grade = st.number_input("Curricular First Semester Grade", min_value=0, max_value=30, step=1)

col1, col2 = st.columns(2)
with col1:
    curricular_2nd_sem_approved = st.number_input("Curricular Second Semester Approved", min_value=0, max_value=30, step=1)
with col2:
    curricular_2nd_sem_grade = st.number_input("Curricular Secod Semester Grade", min_value=0, max_value=30, step=1)

if st.button("Predict"):    
    input_data = np.array([[marital_mapping[marital_status], yes_no_mapping[debtor], yes_no_mapping[tuition], yes_no_mapping[scholarship], attendance_mapping[attend],
                            curricular_1st_sem_approved, curricular_1st_sem_grade,
                            curricular_2nd_sem_approved, curricular_2nd_sem_grade]])    
    
    prediction = model.predict(input_data)   
    st.write("Prediction :", prediction)