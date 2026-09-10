# Customer Churn Prediction

An end-to-end data science project that analyzes customer churn and builds a machine-learning model to identify customers at higher risk of leaving.

## Project Goal

The objective is to:
- Explore customer behavior and churn patterns
- Identify factors associated with churn
- Build a classification model
- Evaluate model performance using precision, recall and ROC-AUC
- Provide actionable business recommendations

## Dataset

This repository contains a synthetic telecom-style customer dataset with 3,000 records.

Important features include:
- Tenure
- Monthly charges
- Contract type
- Internet service
- Payment method
- Tech support
- Paperless billing
- Churn

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SQL
- Jupyter Notebook

## Workflow

1. Data loading
2. Data quality checks
3. Exploratory data analysis
4. Missing-value handling
5. Feature preprocessing
6. Logistic Regression classification
7. Model evaluation
8. Business recommendations

## Key Business Questions

- Which contract types have the highest churn?
- Does customer tenure influence churn?
- Are higher monthly charges associated with churn?
- Which payment methods are associated with greater churn?
- Which customers should be prioritized for retention?

## Running the Project

```bash
git clone <your-repository-url>
cd customer-churn-prediction
pip install -r requirements.txt
jupyter notebook
```

Run `notebooks/customer_churn_analysis.py` as a Python script, or copy the cells into a Jupyter Notebook.

## Example Recommendations

Potential retention strategies include:
- Targeting month-to-month customers with loyalty offers
- Providing onboarding support during the first year
- Reviewing pricing for high-charge customers
- Encouraging longer-term contracts
- Offering proactive technical support

## Disclaimer

The dataset is synthetic and created for portfolio/educational purposes. It does not represent real customers.
