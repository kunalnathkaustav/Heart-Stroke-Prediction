import pickle
import pandas as pd
import streamlit as st

@st.cache_resource()
def model():
    pipeline = pickle.load(open(r"C:\Users\kunal\Desktop\ML Project\vt_clf.pkl",'rb'))
    return pipeline


st.markdown(''' ## :green[**Heart Stroke-Prediction** 🫀]
            ''')

st.write('---')

st.markdown('''#### :red[**Note**]''',)
st.markdown(''':orange[**This prediction tool is not a substitute for professional medical advice, diagnosis,\
            or treatment. Always seek the advice of your physician or other qualified health\
            providers with any questions you may have regarding a medical condition.**]''')
info = st.button("More Info")

if info:
    st.markdown(''' ## :green[**About the App**]''')
    st.markdown('''
    Welcome to the Heart Stroke Prediction Web App. This tool is designed to help you assess your risk of having a stroke based on various health parameters and lifestyle choices. Early detection of stroke risk can significantly improve outcomes and guide necessary lifestyle changes or medical interventions.

    ### What is a Stroke?
    A stroke occurs when the blood supply to part of your brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. Brain cells begin to die within minutes. A stroke is a medical emergency, and prompt treatment is crucial. Early action can minimize brain damage and potential complications.

    ### Why Predict Stroke Risk?
    Knowing your risk factors for stroke can help you make informed decisions about your health. Risk factors include age, hypertension, heart disease, lifestyle choices, and medical history. By understanding these factors, you can take preventive measures to reduce your risk and seek timely medical advice.

    ### How to Use This App
    1. **Input Your Data:** Use the sidebar to enter your details such as gender, age, hypertension status, heart disease status, marital status, work type, residence type, smoking status, average glucose level, and BMI.
    2. **Submit for Prediction:** After entering your details, click on the "Predict" button.
    3. **View Results:** The app will process your data and provide you with a prediction of your stroke risk. If you have a high risk, it is advisable to consult with a healthcare professional for further evaluation and advice.

    ### Understanding Your Results
    - **No Risk:** This indicates that based on the input data, your risk of having a stroke is low. However, it is always good to maintain a healthy lifestyle and regular medical check-ups.
    - **High Risk:** This suggests that you may have a higher chance of experiencing a stroke. It is crucial to seek medical advice for a comprehensive evaluation and to discuss possible preventive measures.

    ### :red[Note]
    This prediction tool is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health providers with any questions you may have regarding a medical condition.
                
    ### :green[Creator]
    hello!! myself Kunal Kaustav Nath a student of VIT-AP MSc. Data Science created this tool as a part of the Machine Learning mini project for predicting the heart-stroke risk of peoples.           
                ''')
st.write('---')



with st.sidebar:

    st.markdown(''' ## :green[**Select the options**]''')
    gender = st.selectbox("Choose your gender", ("Male", "Female"))
    hypertension = st.selectbox("Do you have Hypertension?", ("Yes", "No"))
    heart_disease = st.selectbox("Do you have Heart Disease?", ("Yes", "No"))
    ever_married = st.selectbox("Are you married?",("Yes", "No"))
    work_type = st.selectbox("What is your work type?", ('Private', 'children', 'Self-employed', 'Govt_job', 'Never_worked'))
    Residence_type = st.selectbox("What is your Residence type?", ("Rural", "Urban"))
    smoking_status = st.selectbox("Enter your smoking status",('formerly smoked', 'Unknown', 'never smoked', 'smokes'))


age = st.slider("How old are you?", 0, 130, 25)
avg_glucose_level = st.number_input("Enter your average glucoselevel",40.0,350.0, 90.0, 1.0)
height = st.number_input("Enter your height (in cms)",0.0,300.0, 100.00, step=  10.0, placeholder= "type here...")
weight = st.number_input("Enter your weight (in kgs)",0.0,300.0,step= 10.0,  placeholder= "type here...")


new_bmi = weight/(height*0.01)**2


data = {
    'gender': gender,
    'age': age,
    'hypertension': 1 if hypertension == "Yes" else 0,
    'heart_disease': 1 if heart_disease == "Yes" else 0,
    'ever_married': ever_married,
    'work_type': work_type,
    'Residence_type': Residence_type,
    'avg_glucose_level': avg_glucose_level,
    'smoking_status': smoking_status,
    'new_bmi': new_bmi
}

st.write('---')
st.markdown('''**Your Data**''')
st.dataframe([data])
st.write('---')


if st.button('Predict'):
    clf = model()
    test_data = pd.DataFrame([data])
    result = clf.predict(test_data)

    if result[0] == 0:
        st.markdown("#### :green[**You have no risk of having heart-stroke**]")
    else:
        st.write("#### :red[**You have high chance of having a stroke**]")



