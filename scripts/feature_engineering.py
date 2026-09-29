"""Engineers features from the cleaned Telco Customer Churn data and
produces the train/test splits used by both models.

Reads datasets/processed/telco_cleaned.csv (output of preprocessing.py).
"""

import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

CLEANED_PATH = "datasets/processed/telco_cleaned.csv"
TARGET = "Churn"
RANDOM_STATE = 42
TEST_SIZE = 0.2

# Add-on services, used to build the HasMultipleServices count feature.
ADD_ON_SERVICES = [
    "MultipleLines",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
]

NUMERIC_COLUMNS = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "AvgMonthlyCharge",
    "HasMultipleServices",
]


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Customers with zero tenure have not been billed a full month yet,
    # so TotalCharges / tenure would divide by zero. Their average
    # monthly spend is best approximated by their current monthly rate.
    df["AvgMonthlyCharge"] = np.where(
        df["tenure"] == 0, df["MonthlyCharges"], df["TotalCharges"] / df["tenure"]
    )

    df["HasMultipleServices"] = (df[ADD_ON_SERVICES] == "Yes").sum(axis=1)

    df["TenureBucket"] = pd.cut(
        df["tenure"],
        bins=[-1, 12, 24, 48, 60, 72],
        labels=["0-12", "13-24", "25-48", "49-60", "61-72"],
    )

    return df


def encode_and_split(df: pd.DataFrame):
    y = df[TARGET]
    X = df.drop(columns=[TARGET])

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    # Fit the scaler on the training split only, to avoid leaking
    # information about the test split into the training process.
    scaler = StandardScaler()
    X_train[NUMERIC_COLUMNS] = scaler.fit_transform(X_train[NUMERIC_COLUMNS])
    X_test[NUMERIC_COLUMNS] = scaler.transform(X_test[NUMERIC_COLUMNS])

    return X_train, X_test, y_train, y_test, scaler


def main() -> None:
    df = pd.read_csv(CLEANED_PATH)
    df = engineer_features(df)
    X_train, X_test, y_train, y_test, scaler = encode_and_split(df)

    X_train.to_csv("datasets/processed/X_train.csv", index=False)
    X_test.to_csv("datasets/processed/X_test.csv", index=False)
    y_train.to_csv("datasets/processed/y_train.csv", index=False)
    y_test.to_csv("datasets/processed/y_test.csv", index=False)
    joblib.dump(scaler, "models/scaler.joblib")

    print(f"Train: {X_train.shape}, Test: {X_test.shape}, Features: {X_train.shape[1]}")


if __name__ == "__main__":
    main()
