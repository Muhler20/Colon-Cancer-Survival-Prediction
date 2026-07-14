<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F766E,100:14B8A6&height=260&section=header&text=Colorectal%20Cancer%20Survival%20Prediction&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Machine%20Learning%20%7C%20Healthcare%20Analytics%20%7C%20XGBoost&descAlignY=56" width="100%" />

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-EC6B23?style=for-the-badge)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Healthcare](https://img.shields.io/badge/Healthcare-Machine%20Learning-14B8A6?style=for-the-badge&logo=googlefit&logoColor=white)]()

<br>

### Predicting Patient Survival Using Machine Learning & Clinical Data

An end-to-end machine learning project that predicts colorectal cancer survival using demographic, clinical, and lifestyle factors. The project explores data preprocessing, feature engineering, model evaluation, explainable AI, and deployment through an interactive Streamlit application.

<br>

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=19&pause=1000&color=14B8A6&center=true&vCenter=true&width=750&lines=89,945+Patient+Records;30+Clinical+%26+Lifestyle+Features;Random+Forest+vs+XGBoost;Interactive+Streamlit+Prediction+Dashboard;Healthcare+Machine+Learning+Project" />
</p>

</div>

---

# 🩺 Project Overview

Colorectal cancer remains one of the leading causes of cancer-related deaths worldwide. Accurate survival prediction enables clinicians to identify high-risk patients earlier, prioritize treatment strategies, and support evidence-based decision making.

This project develops multiple supervised machine learning models capable of predicting colorectal cancer survival from patient demographic information, clinical history, healthcare accessibility, and lifestyle behaviors.

The complete machine learning workflow includes:

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Preprocessing
- 🏷️ Feature Encoding
- ⚖️ Class Imbalance Handling
- 🤖 Machine Learning Model Development
- 📈 Model Evaluation
- 🎯 Feature Importance Analysis
- 🌐 Interactive Streamlit Deployment

---

# 🎯 Objectives

The primary goals of this project were to:

- Predict patient survival outcomes using machine learning
- Compare multiple classification algorithms
- Identify the most influential predictors of survival
- Build an interactive application for real-time predictions
- Demonstrate an end-to-end healthcare data science workflow

---

# 📂 Dataset

The project utilizes a retrospective colorectal cancer dataset containing

| Metric | Value |
|---------|------:|
| Total Patients | **89,945** |
| Features | **30** |
| Target Variable | Survival Status |
| Data Type | Clinical + Demographic + Lifestyle |

The dataset contains information including:

- Age
- BMI
- Cancer Stage
- Physical Activity
- Smoking Status
- Alcohol Consumption
- Diet Type
- Treatment Access
- Insurance Coverage
- Tumor Aggressiveness
- Screening History
- Family History
- Chemotherapy
- Radiotherapy
- Surgery
- Socioeconomic Status

---

# ⚙️ Machine Learning Pipeline

```mermaid
flowchart LR

A[Raw Dataset]
-->B[Data Cleaning]

B-->C[Feature Engineering]

C-->D[Encoding]

D-->E[Train/Test Split]

E-->F[Random Forest]

E-->G[XGBoost]

F-->H[Model Evaluation]

G-->H

H-->I[Feature Importance]

I-->J[Streamlit Dashboard]
```

---

# 🔬 Data Preprocessing

To improve model quality and eliminate potential sources of bias, several preprocessing techniques were performed.

## ✔ Feature Engineering

- Label Encoding for categorical variables
- Feature selection
- Removal of identifier columns
- Removal of target leakage variables
- Feature scaling where appropriate

## ✔ Data Cleaning

- Removed Patient_ID
- Removed post-treatment variables
- Eliminated target leakage features
- Standardized categorical values

## ✔ Dataset Split

```text
Training Set : 80%

Testing Set : 20%
```

---

# 🤖 Models Evaluated

The following supervised learning models were implemented and compared.

| Model | Purpose |
|--------|----------|
| 🌲 Random Forest | Baseline ensemble classifier |
| ⚡ XGBoost (23 Features) | Gradient boosting benchmark |
| ⚡ XGBoost (15 Features) | Reduced feature experiment |
| ⚡ XGBoost (10 Features) | Final production model |
