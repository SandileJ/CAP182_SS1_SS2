"""Cleans the raw Telco Customer Churn dataset.

Reads datasets/raw/Telco-Customer-Churn.csv, fixes column types, drops
the non-predictive customer identifier, and writes a cleaned CSV that
feature_engineering.py builds on.
"""

import pandas as pd

RAW_PATH = "datasets/raw/Telco-Customer-Churn.csv"
CLEANED_PATH = "datasets/processed/telco_cleaned.csv"


def load_raw(path: str = RAW_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # TotalCharges is stored as text and is blank for customers with
    # zero tenure (brand new customers), so those rows become 0 spend
    # rather than being dropped.
    df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])

    df = df.drop(columns=["customerID"])

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df


def main() -> None:
    df = load_raw()
    cleaned = clean(df)
    cleaned.to_csv(CLEANED_PATH, index=False)
    print(f"Cleaned {len(cleaned)} rows, {cleaned.shape[1]} columns -> {CLEANED_PATH}")


if __name__ == "__main__":
    main()
