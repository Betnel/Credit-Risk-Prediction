import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page settings
st.set_page_config(page_title="Credit Risk AI", layout="centered")

@st.cache_resource
def load_model():
    try:
        model = joblib.load('credit_risk_model.pkl')
        cols = joblib.load('model_columns.pkl')
        return model, cols
    except:
        return None, None

model, model_columns = load_model()

st.title("CREDIT RISK PREDICTION APPLICATION")
st.markdown("Enter customer details below to predict the likelihood of loan default.")

if model is None:
    st.error("Model files not found! Please ensure you ran the 'save' cell in your notebook.")
else:
    # 2-column layout for inputs
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 35)
        income = st.number_input("Annual Income ($)", 0, 1000000, 50000)
        loan_amount = st.number_input("Loan Amount ($)", 0, 1000000, 15000)
        credit_score = st.slider("Credit Score", 300, 850, 650)
        months_employed = st.number_input("Months Employed", 0, 600, 24)
        num_credit_lines = st.number_input("Number of Credit Lines", 0, 20, 3)

    with col2:
        loan_term = st.number_input("Loan Term (Months)", 1, 360, 60)
        num_late_payments = st.number_input("Number of Late Payments", 0, 50, 0)
        dti_ratio = st.slider("DTI Ratio (0.1 to 1.0)", 0.1, 1.0, 0.3)
        interest_rate = st.slider("Interest Rate (%)", 0.0, 35.0, 10.0)
        education = st.selectbox("Education", ["High School", "Bachelor's", "Master's", "PhD"])
        employment = st.selectbox("Employment Type", ["Full-time", "Part-time", "Self-employed", "Unemployed"])

    # Categorical and Binary selections
    marital = st.selectbox("Marital Status", ["Divorced", "Married", "Single"])
    purpose = st.selectbox("Loan Purpose", ["Auto", "Business", "Education", "Home", "Other"])
    
    c1, c2, c3 = st.columns(3)
    mortgage = c1.radio("Has Mortgage?", ["No", "Yes"])
    dependents = c2.radio("Has Dependents?", ["No", "Yes"])
    cosigner = c3.radio("Has Co-Signer?", ["No", "Yes"])

    if st.button("Predict Default Risk", type="primary"):
        # 1. Create a raw dataframe from inputs
        input_data = pd.DataFrame({
            'Age': [age], 'Income': [income], 'LoanAmount': [loan_amount],
            'CreditScore': [credit_score], 'MonthsEmployed': [months_employed],
            'NumCreditLines': [num_credit_lines], 'LoanTerm': [loan_term],
            'NumLatePayments': [num_late_payments], 'DTIRatio': [dti_ratio],
            'InterestRate': [interest_rate], 'Education': [education],
            'EmploymentType': [employment], 'MaritalStatus': [marital],
            'HasMortgage': [1 if mortgage == "Yes" else 0],
            'HasDependents': [1 if dependents == "Yes" else 0],
            'LoanPurpose': [purpose], 'HasCoSigner': [1 if cosigner == "Yes" else 0]
        })

        # 2. Convert categories to dummies
        input_encoded = pd.get_dummies(input_data)
        
        # 3. Align with model columns (This is where the error was happening)
        # We initialize with 0.0 to ensure the type is float from the start
        final_features = pd.DataFrame(0.0, index=[0], columns=model_columns)
        
        for col in input_encoded.columns:
            if col in model_columns:
                final_features[col] = input_encoded[col].astype(float)

        # 4. Final safety check: Force everything to float
        final_features = final_features.astype(float)

        # 5. Predict
        prediction = model.predict(final_features)[0]
        probability = model.predict_proba(final_features)[0][1]

        st.divider()
        if prediction == 1:
            st.error(f" **High Risk of Default!**")
            st.write(f"The model predicts a **{probability:.2%}** probability of default.")
        else:
            st.success(f" **Low Risk - Likely to Repay**")
            st.write(f"The model predicts a **{probability:.2%}** probability of default.")