import streamlit as st
import pandas as pd
import joblib


# ================================
# LOAD MODEL & FEATURES
# ================================
model = joblib.load("salary_gb_model.pkl")
model_features = joblib.load("model_features.pkl")


# ================================
# JOB TITLES (FROM DATASET)
# ================================
JOB_TITLES = [
    "Account Manager", "Accountant", "Administrative Assistant",
    "Business Analyst", "Business Development Manager",
    "Business Intelligence Analyst", "CEO", "Chief Data Officer",
    "Chief Technology Officer", "Content Marketing Manager",
    "Copywriter", "Creative Director", "Customer Service Manager",
    "Customer Service Rep", "Customer Service Representative",
    "Customer Success Manager", "Data Analyst", "Data Engineer",
    "Data Scientist", "Director", "Director of Data Science",
    "Director of Engineering", "Director of Finance",
    "Director of HR", "Director of Marketing",
    "Director of Operations", "Financial Analyst",
    "Finance Manager", "Graphic Designer", "HR Business Partner",
    "HR Manager", "Human Resources Specialist", "IT Manager",
    "IT Support", "Marketing Analyst", "Marketing Coordinator",
    "Marketing Manager", "Operations Analyst", "Operations Manager",
    "Product Designer", "Product Manager", "Project Manager",
    "Research Scientist", "Sales Associate", "Sales Manager",
    "Senior Accountant", "Senior Data Analyst",
    "Senior Data Engineer", "Senior Data Scientist",
    "Senior Financial Analyst", "Senior Marketing Manager",
    "Senior Product Manager", "Senior Software Engineer",
    "Software Developer", "Software Engineer", "Software Manager",
    "Software Project Manager", "Strategy Consultant",
    "Supply Chain Analyst", "Supply Chain Manager",
    "Technical Recruiter", "Technical Support Specialist",
    "Technical Writer", "Training Specialist", "UX Designer",
    "UX Researcher", "VP of Finance", "VP of Operations",
    "Web Developer"
]


# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="Salary Prediction App",
    page_icon="💼",
    layout="centered"
)


# ================================
# CUSTOM STYLING
# ================================
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: #f8fafc;
}
.footer {
    margin-top: 50px;
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
}
.pred-box {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    padding: 20px;
    border-radius: 12px;
    color: white;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# ================================
# HEADER
# ================================
st.markdown("<h1>💼 Salary Prediction System</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='color:#cbd5f5;'>Machine Learning powered salary prediction</p>",
    unsafe_allow_html=True
)

st.divider()


# ================================
# INPUTS
# ================================
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=65, value=30)
    experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=5)

with col2:
    education = st.selectbox(
        "Education Level",
        ["Bachelor's", "Master's", "PhD"]
    )
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

job_title = st.selectbox("Job Title", JOB_TITLES)


# ================================
# PREDICTION
# ================================
st.divider()

if st.button("🚀 Predict Salary", use_container_width=True):

    input_data = pd.DataFrame({
        "Age": [age],
        "Years of Experience": [experience],
        "Education Level": [education],
        "Gender": [gender],
        "Job Title": [job_title]
    })

    input_encoded = pd.get_dummies(input_data)
    input_encoded = input_encoded.reindex(
        columns=model_features,
        fill_value=0
    )

    prediction = model.predict(input_encoded)[0]

    st.markdown(
        f"""
        <div class="pred-box">
            💰 Predicted Salary<br>
            ₹ {prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )


# ================================
# FOOTER
# ================================
st.markdown("""
<div class="footer">
    Built with Machine Learning <br>
    <b>Developed by Farhan</b>
</div>
""", unsafe_allow_html=True)
