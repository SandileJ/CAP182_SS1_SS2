# Model 1: Logistic Regression

The interpretable baseline model. Chosen because it is easy to explain to a non-technical stakeholder and gives a natural point of comparison for a more complex model.

## Details

- **Technique**: Logistic Regression (`sklearn.linear_model.LogisticRegression`) with L2 regularisation, scikit-learn's default penalty for the `lbfgs` solver.
- **Hyperparameters**: `C=1.0` (inverse regularisation strength), `solver="lbfgs"`, `max_iter=1000`, `class_weight="balanced"`, `random_state=42`.
- **Class imbalance handling**: `class_weight="balanced"` re-weights the loss function so the minority class (churned customers, about 26.5% of the dataset) is not underweighted, as a simpler alternative to the SMOTE oversampling used in the Part A literature.

## File

`scripts/model1_logistic_regression.py`

## How to use it

Run after `feature_engineering.py` has produced the train/test split:

```
python scripts/model1_logistic_regression.py
```

Trains the model, saves it to `models/model1_logistic_regression.joblib`, and saves test set predictions (true label, predicted label, predicted probability) to `datasets/processed/model1_predictions.csv` for use in Part C's performance evaluation.
