💼 Salary Prediction System
Machine Learning • Gradient Boosting • Streamlit

A production-ready machine learning web application that predicts employee salaries based on experience, education, job role, age, and gender.
Built using a tuned Gradient Boosting model and deployed with Streamlit.

✨ Project Highlights

🔍 End-to-end ML workflow (EDA → Modeling → Deployment)

🧠 Hyperparameter tuning using GridSearchCV

📊 Trained on real-world structured data

🎯 Dropdown-based inputs (no invalid entries)

🚀 Fully deployable Streamlit app

🧠 Problem Statement

Salary estimation is often subjective and inconsistent.
This project applies machine learning to predict salaries in a data-driven and transparent way using historical employee data.

🛠️ Machine Learning Pipeline
🔹 Exploratory Data Analysis (EDA)

Salary distribution analysis

Experience vs Salary relationship

Impact of education and job roles

Outlier detection and removal

🔹 Data Preprocessing

Removed missing values

Removed unrealistic salary values

One-Hot Encoding for categorical variables

Train–Test split (80/20)

🔹 Model Training

The following regression models were trained and evaluated:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor (Final Model)

🔹 Hyperparameter Tuning

Used GridSearchCV (5-fold cross-validation)

Tuned parameters:

n_estimators

learning_rate

max_depth

min_samples_leaf

🔹 Model Selection

Gradient Boosting achieved the highest test R²

Best balance between bias and variance

Selected as the final model

🏆 Final Model Details

Algorithm: Gradient Boosting Regressor

Evaluation Metric: R² Score

Tuning Method: GridSearchCV

Model Saved Using: joblib

🖥️ Streamlit Web Application
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
├── requirements.txt           # Dependencies
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

Set app.py as the entry point

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
