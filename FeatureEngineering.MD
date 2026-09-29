# Feature Engineering

Builds model-ready features from the cleaned dataset and produces the train/test split both models use.

## What it does

- **AvgMonthlyCharge**: `TotalCharges / tenure`, using `MonthlyCharges` directly for customers with zero tenure to avoid dividing by zero.
- **HasMultipleServices**: a count of how many add-on services (multiple lines, online security, online backup, device protection, tech support, streaming TV, streaming movies) the customer has, rather than treating each as an independent flag.
- **TenureBucket**: tenure grouped into 0-12, 13-24, 25-48, 49-60, and 61-72 month bands, since churn risk tends to move in bands rather than linearly with tenure.
- One-hot encodes all remaining categorical columns.
- Splits into an 80/20 train/test set, stratified on `Churn` so both splits keep the same churn rate.
- Fits a `StandardScaler` on the numeric columns (`tenure`, `MonthlyCharges`, `TotalCharges`, `AvgMonthlyCharge`, `HasMultipleServices`) using the training split only, then applies it to both splits, so no information from the test set leaks into training.

## File

`scripts/feature_engineering.py`

## How to use it

Run after `preprocessing.py` has produced `datasets/processed/telco_cleaned.csv`:

```
python scripts/feature_engineering.py
```

Writes `datasets/processed/X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`, and saves the fitted scaler to `models/scaler.joblib`.
