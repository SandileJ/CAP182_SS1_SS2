# Model 2: XGBoost

A gradient boosted tree ensemble, chosen to capture non-linear feature interactions that Logistic Regression cannot, and to give a real ensembling comparison against the linear baseline.

## Details

- **Technique**: Gradient boosted decision trees (`xgboost.XGBClassifier`).
- **Hyperparameters**: `n_estimators=200`, `max_depth=4`, `learning_rate=0.05`, `subsample=0.8`, `colsample_bytree=0.8`, `eval_metric="logloss"`, `random_state=42`. Depth is kept shallow (4) and subsampling is used on both rows and columns to reduce overfitting risk on a dataset of this size.
- **Class imbalance handling**: `scale_pos_weight` is computed from the actual training split (ratio of non-churned to churned customers, about 2.77) rather than hardcoded, mirroring the `class_weight="balanced"` approach used in Model 1 so the two models handle imbalance comparably.

## File

`scripts/model2_xgboost.py`

## How to use it

Run after `feature_engineering.py` has produced the train/test split:

```
python scripts/model2_xgboost.py
```

Trains the model, saves it to `models/model2_xgboost.joblib`, and saves test set predictions (true label, predicted label, predicted probability) to `datasets/processed/model2_predictions.csv` for use in Part C's performance evaluation.
