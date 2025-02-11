import os
import pickle # pre trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu 

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")
diabetes_model= pickle.load(open(r"C:\Users\viraj\AICT diesease predict\savedfiles\diebetes_model.sav",'rb'))
heart_disease_model=pickle.load(open(r"C:\Users\viraj\AICT diesease predict\savedfiles\heartdisease_model.sav",'rb'))
parkinsons_model= pickle.load(open(r"C:\Users\viraj\AICT diesease predict\savedfiles\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI  value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of the person')

diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
    user_input= [float(x) for x in user_input]
    diab_prediction= diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis= 'The person is diabetic'
    else:
        diab_diagnosis= 'The person is not diabetic'
st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        resting_bp = st.text_input('Resting Blood Pressure')
        rest_ecg = st.text_input('Resting Electrocardiographic Results')
        st_depression = st.text_input('ST Depression Induced by Exercise')
    with col2:
        sex = st.text_input('Sex (1 = male, 0 = female)')
        serum_cholesterol = st.text_input('Serum Cholesterol in mg/dl')
        max_heart_rate = st.text_input('Maximum Heart Rate Achieved')
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        chest_pain = st.text_input('Chest Pain Types (0-3)')
        fasting_blood_sugar = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)')
        exercise_angina = st.text_input('Exercise Induced Angina (1 = yes, 0 = no)')
        major_vessels = st.text_input('Major Vessels Colored by Fluoroscopy (0-3)')

    thal = st.text_input('Thal (0 = normal, 1 = fixed defect, 2 = reversible defect)')

    # Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, chest_pain, resting_bp, serum_cholesterol, fasting_blood_sugar,
                      rest_ecg, max_heart_rate, exercise_angina, st_depression, slope,
                      major_vessels, thal]

        # Convert inputs to float
        try:
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does not have heart disease'

            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")



# Parkinson's Disease Prediction Page
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo = st.text_input('MDVP (Hz)')
        MDVP_Shimmer = st.text_input('MDVP Shimmer')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')
    with col2:
        MDVP_Fhi = st.text_input('MDVP (Hz)')
        MDVP_Jitter = st.text_input('MDVP Jitter')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')
    with col3:
        MDVP_Flo = st.text_input('MDVP (Hz)')
        MDVP_dB = st.text_input('MDVP (dB)')
        DFA = st.text_input('DFA')
        Spread1 = st.text_input('Spread1')
        Spread2 = st.text_input('Spread2')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Shimmer, MDVP_dB, HNR, RPDE, DFA, Spread1, Spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has Parkinson’s disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinson’s disease'

    st.success(parkinsons_diagnosis)
