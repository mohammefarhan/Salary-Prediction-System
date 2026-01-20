💼 Salary Prediction System
Machine Learning • Gradient Boosting • Streamlit

A production-ready machine learning web application that predicts employee salaries based on experience, education, job role, age, and gender.
Built with a tuned Gradient Boosting model and deployed using Streamlit.

✨ Project Highlights

🔍 End-to-end ML workflow (EDA → Modeling → Deployment)

🧠 Tuned using GridSearchCV

📊 Trained on real-world structured data

🎯 Clean UI with dropdown-based inputs (no invalid entries)

🚀 Deployment-ready Streamlit app

🧠 Problem Statement

Salary estimation is often subjective and inconsistent.
This project aims to predict salaries accurately using historical data and machine learning, providing a transparent and data-driven approach.

🛠️ Machine Learning Pipeline
🔹 1. Exploratory Data Analysis (EDA)

Salary distribution analysis

Experience vs Salary trends

Education & Job Title impact

Outlier detection and removal

🔹 2. Data Preprocessing

Removed missing values

Removed unrealistic salary values

One-Hot Encoding for categorical variables

Train–Test split (80/20)

🔹 3. Model Training

Four regression models were trained and evaluated:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor (Final Model)

🔹 4. Hyperparameter Tuning

Used GridSearchCV (5-fold cross-validation)

Optimized:

n_estimators

learning_rate

max_depth

min_samples_leaf

🔹 5. Model Selection

Gradient Boosting achieved the highest test R²

Best balance between bias and variance

Selected as the final model

🏆 Final Model Details

Algorithm: Gradient Boosting Regressor

Metric Used: R² Score

Tuning: GridSearchCV

Model Saved Using: joblib

🖥️ Streamlit Web App
App Features

🔢 Numeric inputs for Age & Experience

📚 Dropdowns for Education, Gender, and Job Title

🧩 Automatic feature alignment (prevents inference errors)

🎨 Modern dark-themed UI

💰 Highlighted salary prediction output

📁 Project Structure
├── app.py                     # Streamlit web app
├── salary_gb_model.pkl        # Trained Gradient Boosting model
├── model_features.pkl         # Feature list for inference alignment
├── Salary Data.csv            # Dataset
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation

⚙️ Installation & Usage
1️⃣ Clone the repository
git clone https://github.com/your-username/salary-prediction-app.git
cd salary-prediction-app

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app locally
streamlit run app.py

☁️ Deployment (Streamlit Cloud)

Push the project to GitHub

Go to 👉 https://streamlit.io/cloud

Select the repository

Set app.py as the main file

Deploy 🚀

🧰 Tech Stack

Python

Pandas, NumPy

Scikit-learn

Gradient Boosting

GridSearchCV

Streamlit

Joblib

👤 Author

Farhan
Machine Learning | Data Science | Python

Built with ❤️ using Machine Learning & Streamlit
