Credit Risk Prediction & Analysis

An end-to-end Machine Learning solution designed to predict loan default risks using financial and demographic customer data.
Project Overview

This project addresses the critical challenge of credit risk assessment in the financial sector. Using a dataset of over 250,000 records, I developed a robust predictive model that identifies potential loan defaulters with high precision.

The project transitions from a comprehensive exploratory analysis in a Jupyter Notebook to a production-ready interactive application deployed using Streamlit.

The solution enables financial institutions to automate risk assessment, improve lending decisions, and reduce exposure to high-risk borrowers.
Live Demo

🔗 Access the Credit Risk Predictor App

https://credit-risk-prediction-jffbjcq2ddxayyumemx86l.streamlit.app/
Technologies Used
Programming & Data Science

    Python
    Pandas
    NumPy
    Scikit-Learn

Machine Learning

    XGBoost
    Logistic Regression
    Random Forest

Data Visualization

    Matplotlib
    Seaborn
    Plotly

Deployment & Version Control

    Streamlit
    GitHub

Technical Workflow
1. Data Understanding & Engineering
Data Cleaning

    Removed non-informative columns such as LoanID
    Handled missing values and inconsistencies

Feature Engineering

    Converted binary categories:
        HasMortgage
        HasDependents
        HasCoSigner

into numerical representations.

    Applied feature preprocessing for categorical and numerical variables.

Exploratory Data Analysis (EDA)

Performed extensive analysis to understand:

    Loan default behavior
    Correlations between variables
    Risk-driving financial indicators
    Customer demographic trends

Visualizations were created to identify:

    Income distributions
    Credit score patterns
    Interest rate impacts
    Loan amount relationships

Model Development

Multiple machine learning models were tested and evaluated.
Models Implemented
Logistic Regression

Used as the baseline classification model.
Random Forest

Implemented to capture non-linear feature interactions.
XGBoost (Final Selected Model)

Chosen due to superior predictive performance and robustness on imbalanced data.

Key optimization techniques:

    Hyperparameter tuning
    scale_pos_weight handling
    Feature preprocessing
    Threshold tuning

Model Evaluation Metrics

The project focused on metrics that are highly important in credit risk systems:

    Recall
    Precision
    F1 Score
    accuracy score
    confusion matrix

Special emphasis was placed on Recall to minimize false negatives and ensure high-risk borrowers are properly identified.
Streamlit Application

An interactive web application was developed using Streamlit to make the model accessible to end users.
App Features
Single Customer Prediction

Predict whether an individual customer is likely to default.
Batch CSV Prediction

Upload a CSV file containing multiple customers for bulk risk analysis.
Default Probability Scoring

Displays the probability of default for each applicant.
Interactive Dashboard

Provides analytics and visual insights into the dataset.
Download Predictions

Users can export prediction results as CSV files.
Responsive User Interface

Clean dashboard layout suitable for business presentations and demonstrations.
Business Insights

The analysis revealed several important drivers of loan default risk.
Major Risk Indicators

    Lower credit scores significantly increase default probability.
    High interest rates correlate strongly with loan defaults.
    Lower income levels increase financial vulnerability.
    Employment instability is a strong predictor of repayment challenges.
    Higher loan amounts increase lending exposure.

Strategic Business Value

This system can help financial institutions:

    Automate initial loan screening
    Reduce manual risk assessment workload
    Improve decision consistency
    Minimize credit losses
    Accelerate loan approval workflows
    Support data-driven lending strategies

Project Structure

ML PROJECTS/
│
├── credit_risk_prediction.ipynb   # Research, EDA, and model experimentation
├── Loan_default.csv               # Dataset
├── train_model.py                 # Model training pipeline
├── app.py                         # Streamlit application
├── model.pkl                      # Trained machine learning model
├── preprocessor.pkl               # Saved preprocessing pipeline
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

Local Setup
1. Clone the Repository

git clone https://github.com/BrentOchieng/Credit-Risk-Prediction.git

2. Navigate Into the Project

cd Credit-Risk-Prediction

3. Install Dependencies

pip install -r requirements.txt

4. Train the Model

python train_model.py

This generates:

model.pkl
preprocessor.pkl

5. Run the Streamlit App

streamlit run app.py

6. Open in Browser

http://localhost:8501

Deployment

The application can be deployed using:

    Streamlit Community Cloud
    Render
    Railway
    AWS
    Azure

Future Improvements

Potential future enhancements include:

    SHAP explainability integration
    User authentication system
    Real-time database integration
    Cloud API deployment
    Automated model retraining
    Advanced monitoring dashboards


