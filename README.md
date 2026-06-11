# Credit Risk Prediction Application

## Project Overview

This project is an end-to-end Machine Learning application that predicts the likelihood of a borrower defaulting on a loan based on demographic, financial, and credit-related information.

The solution combines data preprocessing, feature engineering, machine learning model development, model serialization, and deployment through an interactive Streamlit web application.

The goal is to demonstrate a complete Data Science workflow, from raw data to a production-ready predictive application that can support credit risk assessment and lending decisions.

---

## Problem Statement

Financial institutions face significant losses due to loan defaults. Accurately identifying high-risk borrowers before loan approval helps lenders:

- Reduce credit losses
- Improve portfolio quality
- Enhance risk management strategies
- Make data-driven lending decisions
- Improve financial inclusion through objective assessments

This project uses machine learning techniques to classify borrowers as either:

- **Low Risk (Likely to Repay)**
- **High Risk (Likely to Default)**

---

## Project Objectives

The main objectives of this project were:

- Build a predictive model for loan default risk.
- Explore borrower financial and demographic characteristics.
- Identify key factors influencing credit risk.
- Deploy an interactive application for real-time predictions.
- Demonstrate an end-to-end Machine Learning workflow suitable for production environments.

----
### Launch Live Demo

-https://credit-risk-prediction-lftkmuzsjrak3t96mygoey.streamlit.app/
---

## Dataset Description

The model uses borrower-level information including:

### Demographic Features

- Age
- Marital Status
- Education Level
- Employment Type

### Financial Features

- Annual Income
- Loan Amount
- Interest Rate
- Debt-to-Income Ratio (DTI)

### Credit History Features

- Credit Score
- Number of Credit Lines
- Number of Late Payments
- Months Employed

### Additional Loan Features

- Loan Term
- Loan Purpose
- Mortgage Status
- Dependents
- Co-Signer Availability

---

## Project Workflow

### 1. Data Understanding

The dataset was explored to understand:

- Data structure
- Missing values
- Variable distributions
- Target variable balance
- Potential risk indicators

### 2. Data Cleaning

Performed:

- Data validation
- Handling missing values
- Data type corrections
- Feature consistency checks

### 3. Exploratory Data Analysis (EDA)

Explored relationships between:

- Income and default risk
- Credit score and repayment behavior
- Debt burden and loan performance
- Employment history and default probability

Visualizations were used to identify trends, patterns, and risk factors.

### 4. Feature Engineering

Categorical variables were transformed using:

- One-Hot Encoding (`pd.get_dummies()`)

Binary variables were converted into numerical representations for model compatibility.

### 5. Model Development

Several machine learning techniques were evaluated to determine the best-performing model for classification.

The final model was trained using engineered borrower features and optimized for predictive performance.

### 6. Model Serialization

The trained model and feature structure were saved using:

- Joblib

Files generated:

```python
credit_risk_model.pkl
model_columns.pkl
```

These files are loaded directly by the Streamlit application during prediction.

### 7. Deployment

The model was deployed using Streamlit to provide an interactive user interface where users can:

- Enter borrower information
- Generate predictions instantly
- View default risk probability
- Interpret risk outcomes

---

## Application Features

### Borrower Information Input

The application allows users to enter:

#### Personal Information

- Age
- Marital Status
- Education Level

#### Employment Information

- Employment Type
- Months Employed

#### Financial Information

- Annual Income
- Loan Amount
- Interest Rate
- Debt-to-Income Ratio

#### Credit Information

- Credit Score
- Number of Credit Lines
- Number of Late Payments

#### Loan Information

- Loan Term
- Loan Purpose

#### Additional Risk Indicators

- Mortgage Status
- Dependents
- Co-Signer Availability

---

## Prediction Process

The application performs the following steps:

### Step 1: User Input Collection

User inputs are captured through Streamlit widgets.

### Step 2: Feature Encoding

Categorical features are converted into numerical representations using one-hot encoding.

### Step 3: Feature Alignment

Input features are aligned with the exact feature structure used during model training.

This ensures:

- Consistent feature ordering
- No missing columns
- Compatibility with the trained model

### Step 4: Prediction

The model generates:

- Predicted class
- Default probability score

### Step 5: Results Display

The application displays:

#### Low Risk

```text
Low Risk - Likely to Repay
```

along with the estimated probability of default.

#### High Risk

```text
High Risk of Default
```

along with the estimated probability of default.

---

## Technology Used

### Programming Language

- Python

### Data Analysis
-Matplotlib
-Seaborn
-Plotly

### Machine Learning
-XGBoost
-Logistic Regression
-Random Forest
### Model Serialization

- Joblib

### Deployment

- Streamlit

---

## Project Structure

```text
Credit-Risk-Prediction/
│
├── app.py
├── credit_risk_model.pkl
├── model_columns.pkl
├── requirements.txt
├── README.md
│
└── notebooks/
    └── credit_risk_prediction.ipynb
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Betnel/Credit-Risk-Prediction.git
```

### Navigate to Project Directory

```bash
cd Credit-Risk-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Launch the Streamlit application locally:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Example Use Case

A loan officer receives a new loan application and enters the applicant's:

- Income
- Credit score
- Employment history
- Loan amount
- Debt ratio

The model evaluates the applicant's profile and returns:

- Default risk classification
- Estimated probability of default

This supports faster and more consistent lending decisions.

---

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Classification modeling
- Model evaluation
- Model deployment
- Building production-ready Streamlit applications
- End-to-end Machine Learning workflows

---

## Future Improvements

Potential enhancements include:

- Model explainability using SHAP
- Feature importance visualization
- Loan approval recommendations
- Risk segmentation dashboard
- Real-time API deployment
- Cloud deployment using AWS or Azure
- Integration with financial institution databases

---

## Author

**Nelvin Bett**

Data Analyst | Aspiring Data Scientist

### Connect With Me

- LinkedIn: www.linkedin.com/in/nelvin-bett


---


