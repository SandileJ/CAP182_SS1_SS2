"""Trains Model 2, an XGBoost classifier, on the engineered Telco
Customer Churn features and saves the fitted model plus test set
predictions for later performance evaluation.
"""

import joblib
import pandas as pd
from xgboost import XGBClassifier

X_TRAIN_PATH = "datasets/processed/X_train.csv"
X_TEST_PATH = "datasets/processed/X_test.csv"
Y_TRAIN_PATH = "datasets/processed/y_train.csv"
Y_TEST_PATH = "datasets/processed/y_test.csv"

MODEL_PATH = "models/model2_xgboost.joblib"
PREDICTIONS_PATH = "datasets/processed/model2_predictions.csv"

BASE_PARAMS = dict(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42,
)


def main() -> None:
    X_train = pd.read_csv(X_TRAIN_PATH)
    X_test = pd.read_csv(X_TEST_PATH)
    y_train = pd.read_csv(Y_TRAIN_PATH).squeeze()
    y_test = pd.read_csv(Y_TEST_PATH).squeeze()

    # scale_pos_weight rebalances the gradient boosting loss for the
    # minority churn class, computed from the actual training split
    # rather than hardcoded, mirroring the class_weight="balanced"
    # approach used in Model 1.
    scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

    model = XGBClassifier(scale_pos_weight=scale_pos_weight, **BASE_PARAMS)
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

    print(f"Model 2 (XGBoost) trained on {len(X_train)} rows, scale_pos_weight={scale_pos_weight:.3f}")
    print(f"Model saved to {MODEL_PATH}")
    print(f"Test set predictions saved to {PREDICTIONS_PATH}")


if __name__ == "__main__":
    main()
