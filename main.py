# ================================
# 1. IMPORTS
# ================================
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor


# ================================
# 2. LOAD DATA
# ================================
df = pd.read_csv("Salary Data.csv")


# ================================
# 3. DATA CLEANING
# ================================
df = df.dropna()
df = df[df["Salary"] > 10000]
df = df.reset_index(drop=True)


# ================================
# 4. FEATURE SELECTION
# ================================
X = df[[
    "Age",
    "Years of Experience",
    "Education Level",
    "Gender",
    "Job Title"
]]

y = df["Salary"]


# ================================
# 5. ONE-HOT ENCODING
# ================================
X = pd.get_dummies(X)


# ================================
# 6. TRAIN TEST SPLIT
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# ================================
# 7. BASE MODEL
# ================================
gb = GradientBoostingRegressor(random_state=42)


# ================================
# 8. GRID SEARCH PARAMETERS
# ================================
param_grid = {
    "n_estimators": [200, 300, 500],
    "learning_rate": [0.05, 0.1],
    "max_depth": [2, 3, 4],
    "min_samples_leaf": [1, 3, 5]
}


# ================================
# 9. GRID SEARCH CV
# ================================
grid_gb = GridSearchCV(
    estimator=gb,
    param_grid=param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1,
    verbose=1
)

grid_gb.fit(X_train, y_train)


# ================================
# 10. BEST MODEL
# ================================
final_gb_model = grid_gb.best_estimator_


# ================================
# 11. EVALUATION
# ================================
train_r2 = final_gb_model.score(X_train, y_train)
test_r2 = final_gb_model.score(X_test, y_test)

print("Best Parameters:", grid_gb.best_params_)
print("Train R2:", train_r2)
print("Test R2:", test_r2)


# ================================
# 12. SAVE MODEL & FEATURES
# ================================
joblib.dump(final_gb_model, "salary_gb_model.pkl")
joblib.dump(X_train.columns.tolist(), "model_features.pkl")

print("Model and feature list saved successfully.")
