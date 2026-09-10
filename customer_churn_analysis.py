# Customer Churn Prediction
# End-to-end data science project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

df = pd.read_csv("../data/customer_churn.csv")

print(df.head())
print(df.info())
print(df["churn"].value_counts(normalize=True))

# Basic EDA
print(df.groupby("contract")["churn"].apply(lambda x: (x == "Yes").mean()).sort_values(ascending=False))

# Numeric distributions
df[["tenure_months", "monthly_charges", "total_charges"]].hist(figsize=(10, 7))
plt.tight_layout()
plt.show()

# Prepare target/features
X = df.drop(columns=["customer_id", "churn"])
y = (df["churn"] == "Yes").astype(int)

numeric_features = ["senior_citizen", "tenure_months", "monthly_charges", "total_charges"]
categorical_features = [c for c in X.columns if c not in numeric_features]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model.fit(X_train, y_train)

pred = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, pred))
print("ROC-AUC:", round(roc_auc_score(y_test, proba), 4))
print("Confusion matrix:\n", confusion_matrix(y_test, pred))

# Save model
import joblib
joblib.dump(model, "../models/churn_model.joblib")
print("Model saved to ../models/churn_model.joblib")
