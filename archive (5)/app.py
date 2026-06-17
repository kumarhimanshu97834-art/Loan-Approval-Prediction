import streamlit as st
import pickle
import pandas as pd

# Load Model
model = pickle.load(open("loan_approval_model.pkl", "rb"))

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Loan Approval Prediction System")
st.markdown("Predict whether a loan application will be Approved or Rejected.")

st.sidebar.header("Applicant Information")

no_of_dependents = st.sidebar.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    value=2
)

education = st.sidebar.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.sidebar.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

income_annum = st.sidebar.number_input(
    "Annual Income",
    min_value=0
)

loan_amount = st.sidebar.number_input(
    "Loan Amount",
    min_value=0
)

loan_term = st.sidebar.number_input(
    "Loan Term"
)

cibil_score = st.sidebar.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900
)

residential_assets_value = st.sidebar.number_input(
    "Residential Assets Value",
    min_value=0
)

commercial_assets_value = st.sidebar.number_input(
    "Commercial Assets Value",
    min_value=0
)

luxury_assets_value = st.sidebar.number_input(
    "Luxury Assets Value",
    min_value=0
)

bank_asset_value = st.sidebar.number_input(
    "Bank Asset Value",
    min_value=0
)

# Encoding
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

# Feature Engineering
loan_income_ratio = loan_amount / income_annum if income_annum > 0 else 0

total_assets = (
    residential_assets_value
    + commercial_assets_value
    + luxury_assets_value
    + bank_asset_value
)

loan_per_term = loan_amount / loan_term if loan_term > 0 else 0

input_data = pd.DataFrame({
    'no_of_dependents':[no_of_dependents],
    'education':[education],
    'self_employed':[self_employed],
    'income_annum':[income_annum],
    'loan_amount':[loan_amount],
    'loan_term':[loan_term],
    'cibil_score':[cibil_score],
    'residential_assets_value':[residential_assets_value],
    'commercial_assets_value':[commercial_assets_value],
    'luxury_assets_value':[luxury_assets_value],
    'bank_asset_value':[bank_asset_value],
    'loan_income_ratio':[loan_income_ratio],
    'total_assets':[total_assets],
    'loan_per_term':[loan_per_term]
})

if st.button("Predict Loan Status"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.subheader("Applicant Details")
    st.dataframe(input_data)