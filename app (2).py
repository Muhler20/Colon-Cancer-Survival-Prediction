import streamlit as st
import pandas as pd
import numpy as np
import pickle

# page configuration
st.set_page_config(page_title="CRC Survival Prediction Dashboard", layout="wide")

# load trained objects
model = pickle.load(open(r"C:\Users\micha\OneDrive\Desktop\Coding Projects\Colon Prediction Model\xgb_11.pkl","rb"))
features = pickle.load(open(r"C:\Users\micha\OneDrive\Desktop\Coding Projects\Colon Prediction Model\features_11.pkl","rb"))

# displaying necessary information about model on UI interface
st.title("🩺 Colorectal Cancer Survival Prediction Dashboard")
st.markdown("""
<div style='padding:15px; border-radius:10px; background-color:blue;'>
<b>About the Model</b><br>
This model predicts colorectal cancer survival probability using different types of factors as indicated on the left sidebar. Risk categories are determined based on predicted 
survival probability.
</div>
""", unsafe_allow_html=True)

st.subheader("Please enter patient details on left side to estimate survival probability. All fields are mandatory for best prediction")

# map input category to numerics
stage_at_diagnosos_map = {"Stage I":0, "Stage II":1, "Stage III":2, "Stage IV":3}
diet_type_map = {"Balanced":0, "Traditional-Low":1, "Western-High":2}
physical_activity_level_map = {"Low":0, "Medium":1, "High":2}
smoking_status_map = {'Current':0, 'Former':1, 'Never':2}
alcohol_consumption_map = {"Low":0, "Medium":1, "High":2}
red_meat_consumption_map = {"Low":0, "Medium":1, "High":2}
insurance_coverrage_map = {'No':0, 'Yes':1}
time_to_diagnosis_map = {'Delayed':0, 'Timely':1} 

# take patient inputs entered by user
# sidebar inputs on left side of dashboard
st.sidebar.header("📝 Patient Inputs")
age = st.sidebar.slider("Age",18,90,50)
bmi = st.sidebar.slider("BMI",15.0,40.0,25.0)
stage_at_diagnosis_label = st.sidebar.selectbox("Stage at Diagnosis", list(stage_at_diagnosos_map.keys()))
time_to_diagnosis_label = st.sidebar.selectbox("Time to Diagnosis", list(time_to_diagnosis_map.keys()))
insurance_coverage_label = st.sidebar.selectbox("Insurance Coverage", list(insurance_coverrage_map.keys()))
diet_type_label = st.sidebar.selectbox("Diet Type", list(diet_type_map.keys()))
physical_activity_level_label = st.sidebar.selectbox("Physical Activity Level", list(physical_activity_level_map.keys()))
smoking_status_label = st.sidebar.selectbox("Smoking Status", list(smoking_status_map.keys()))
alcohol_consumption_label = st.sidebar.selectbox("Alcohol Consumption", list(alcohol_consumption_map.keys()))
red_meat_consumption_label = st.sidebar.selectbox("Red Meat Consumption", list(red_meat_consumption_map.keys()))

# convert categorical labels to numeric
stage_at_diagnosis = stage_at_diagnosos_map[stage_at_diagnosis_label]
diet_type = diet_type_map[diet_type_label]
physical_activity_level = physical_activity_level_map[physical_activity_level_label]
smoking_status = smoking_status_map[smoking_status_label]
alcohol_consumption = alcohol_consumption_map[alcohol_consumption_label]
red_meat_consumption = red_meat_consumption_map[red_meat_consumption_label]
insurance_coverage = insurance_coverrage_map[insurance_coverage_label]
time_to_diagnosis = time_to_diagnosis_map[time_to_diagnosis_label]

# create input dataframe
input_data = pd.DataFrame(np.zeros((1,len(features))), columns=features)

# numeric inputs
input_data["Age"] = age
input_data["BMI"] = bmi
input_data["Stage_at_Diagnosis"] = stage_at_diagnosis
input_data["Diet_Type"] = diet_type
input_data["Physical_Activity_Level"] = physical_activity_level
input_data["Smoking_Status"] = smoking_status
input_data["Alcohol_Consumption"] = alcohol_consumption
input_data["Red_Meat_Consumption"] = red_meat_consumption
input_data["Insurance_Coverage"] = insurance_coverage
input_data["Time_to_Diagnosis"] = time_to_diagnosis

# predicting outcome form preprocessed inputs
st.subheader("⚠️ Risk Category Guide")
col1, col2, col3 = st.columns(3)

with col1:
    st.success("Low Risk | >70% Survival")
with col2:
    st.warning("Moderate Risk | 40–70% Survival")
with col3:
    st.error("High Risk |  <40% Survival")

# displaying patient inputs' summary
st.subheader("🧾 Patient Input Summary")
with st.expander("Show Input Summary"):
    input_summary = {
        "Age": age,
        "BMI": bmi,
        "Stage at Diagnosis": stage_at_diagnosis_label,
        "Time to Diagnosis": time_to_diagnosis_label,
        "Insurance Coverage": insurance_coverage_label,
        "Diet Type": diet_type_label,
        "Physical Activity": physical_activity_level_label,
        "Smoking Status": smoking_status_label,
        "Alcohol Consumption": alcohol_consumption_label,
        "Red Meat Consumption": red_meat_consumption_label
    }
    
    df_summary = pd.DataFrame({"Feature": list(input_summary.keys()),"Value": list(input_summary.values())})
    df_summary["Value"] = df_summary["Value"].astype(str)
    st.dataframe(df_summary, width="stretch")

st.subheader("📊 Prediction Results")
col1, col2 = st.columns(2)
if st.button("🔍 Predict Survival Outcome"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)
    survival_prob = probability[0][1]
    mortality_prob = probability[0][0]
    
    
    with col1:
        st.subheader("1. Prediction Insight")
        if prediction[0] == 1:
            st.success("Patient Likely to Survive")
        else:
            st.error("Patient Not Likely to Survive")

        st.subheader("2. Risk Category")
        if survival_prob > 0.7:
            st.success("🟢 Low Risk")
        elif 0.4 < survival_prob <= 0.7:
            st.warning("🟡 Moderate Risk")
        else:
            st.error("🔴 High Risk")

    with col2:
        # displaying probability
        st.subheader("3. Survival Probability")
        st.progress(float(survival_prob))
        st.write(f"Survival Chance: {survival_prob*100:.2f}%")
        st.write(f"Mortality Risk: {mortality_prob*100:.2f}%")
        chart = pd.DataFrame({
            "Outcome":["Survival","Mortality"],
            "Probability":[survival_prob, mortality_prob]
        })
        st.bar_chart(chart.set_index("Outcome"))

# footer message
st.markdown("---")
st.caption("*Please note that this activity is solely intended for academic purpose and demonstration only.")
st.caption("*This is not permitted to use for real cases.")