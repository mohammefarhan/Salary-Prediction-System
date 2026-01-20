💼 Salary Prediction System (Machine Learning + Streamlit)

A machine learning web application that predicts employee salary based on age, experience, education level, gender, and job title.
The model is trained using Gradient Boosting with GridSearchCV and deployed using Streamlit.

🚀 Live Features

Predict salary in real time

Dropdown-based inputs (no invalid entries)

Trained on real-world structured data

Clean and modern UI

Deployment-ready Streamlit app

🧠 Machine Learning Workflow
1. Exploratory Data Analysis (EDA)

Salary distribution analysis

Experience vs Salary relationship

Education, Gender, and Job Title impact

Outlier handling and data cleaning

2. Data Preprocessing

Removed missing values

Removed unrealistic salary entries

One-Hot Encoding for categorical features

Train-test split (80/20)

3. Model Building

Four regression models were trained and evaluated:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor (Final Model)

4. Hyperparameter Tuning

Used GridSearchCV (5-fold cross-validation)

Optimized:

n_estimators

learning_rate

max_depth

min_samples_leaf

5. Model Selection

Gradient Boosting achieved the highest test R²

Best balance between bias and variance

Selected as final model

🏆 Final Model

Algorithm: Gradient Boosting Regressor

Tuning Method: GridSearchCV

Metric: R² Score

Saved using: joblib

🖥️ Web Application (Streamlit)

The trained model is deployed as an interactive Streamlit app.

App Features:

Numeric inputs for Age & Experience

Dropdowns for Education, Gender, and Job Title

Automatic feature alignment to avoid prediction errors

Styled UI with prediction highlight

📁 Project Structure
├── app.py                     # Streamlit application
├── salary_gb_model.pkl        # Trained Gradient Boosting model
├── model_features.pkl         # Feature list for column alignment
├── Salary Data.csv            # Dataset
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
