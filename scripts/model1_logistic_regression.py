"""Trains Model 1, a Logistic Regression classifier, on the engineered
Telco Customer Churn features and saves the fitted model plus test
set predictions for later performance evaluation.
"""

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

X_TRAIN_PATH = "datasets/processed/X_train.csv"
X_TEST_PATH = "datasets/processed/X_test.csv"
Y_TRAIN_PATH = "datasets/processed/y_train.csv"
Y_TEST_PATH = "datasets/processed/y_test.csv"

MODEL_PATH = "models/model1_logistic_regression.joblib"
PREDICTIONS_PATH = "datasets/processed/model1_predictions.csv"

# class_weight="balanced" re-weights the loss to account for churn
# being the minority class (about 26.5% of customers), as an
# alternative to oversampling techniques like SMOTE used in Part A's
# literature. L2 regularisation is scikit-learn's default penalty for
# the lbfgs solver.
MODEL_PARAMS = dict(
    C=1.0,
    solver="lbfgs",
    max_iter=1000,
    class_weight="balanced",
    random_state=42,
)


def main() -> None:
    X_train = pd.read_csv(X_TRAIN_PATH)
    X_test = pd.read_csv(X_TEST_PATH)
    y_train = pd.read_csv(Y_TRAIN_PATH).squeeze()
    y_test = pd.read_csv(Y_TEST_PATH).squeeze()

    model = LogisticRegression(**MODEL_PARAMS)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    predictions = pd.DataFrame(
        {
            "y_true": y_test.values,
            "y_pred": model.predict(X_test),
            "y_proba": model.predict_proba(X_test)[:, 1],
        }
    )
    predictions.to_csv(PREDICTIONS_PATH, index=False)

    print(f"Model 1 (Logistic Regression) trained on {len(X_train)} rows")
    print(f"Model saved to {MODEL_PATH}")
    print(f"Test set predictions saved to {PREDICTIONS_PATH}")


if __name__ == "__main__":
    main()
