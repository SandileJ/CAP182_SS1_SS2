# Preprocessing

Cleans the raw Telco Customer Churn dataset ahead of feature engineering and modelling.

## What it does

- Fixes `TotalCharges`, which is stored as text in the raw file and is blank for the 11 customers with zero tenure (brand new customers). Blanks are set to 0 and the column is converted to numeric.
- Drops `customerID`, since it is a unique identifier with no predictive value.
- Encodes the target column `Churn` from `Yes`/`No` to `1`/`0`.

Categorical encoding, scaling, and the train/test split happen in feature engineering, not here, since those steps depend on the engineered features too.

## File

`scripts/preprocessing.py`

## How to use it

From the repository root, with the dependencies in `requirements.txt` installed:

```
python scripts/preprocessing.py
```

Reads `datasets/raw/Telco-Customer-Churn.csv` and writes `datasets/processed/telco_cleaned.csv`.

Part of the SS2 proof of viability work, which uses this public dataset ahead of the real STADIOchoice data requested in SS1's Part C.
