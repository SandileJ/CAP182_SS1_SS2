"""Evaluates Model 1 (Logistic Regression) on the held-out test set,
using both point metrics and a bootstrap confidence interval on
ROC-AUC as a statistical measure of how stable that estimate is.
"""

import json

import pandas as pd
from sklearn.metrics import roc_auc_score

from metrics_utils import bootstrap_ci, compute_metrics, plot_confusion_matrix, plot_roc_curves

PREDICTIONS_PATH = "datasets/processed/model1_predictions.csv"
METRICS_PATH = "experimental_results/model1_metrics.json"
CONFUSION_MATRIX_PATH = "experimental_results/model1_confusion_matrix.png"
ROC_CURVE_PATH = "experimental_results/model1_roc_curve.png"


def main() -> None:
    predictions = pd.read_csv(PREDICTIONS_PATH)
    y_true = predictions["y_true"]
    y_pred = predictions["y_pred"]
    y_proba = predictions["y_proba"]

    metrics = compute_metrics(y_true, y_pred, y_proba)
    auc_lower, auc_upper = bootstrap_ci(y_true, y_proba, roc_auc_score)
    metrics["roc_auc_95ci_lower"] = auc_lower
    metrics["roc_auc_95ci_upper"] = auc_upper

    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=2)

    plot_confusion_matrix(y_true, y_pred, "Model 1: Logistic Regression", CONFUSION_MATRIX_PATH)
    plot_roc_curves([("Model 1: Logistic Regression", y_true, y_proba)], ROC_CURVE_PATH)

    print("Model 1 (Logistic Regression) performance on the test set:")
    for key, value in metrics.items():
        print(f"  {key}: {value:.4f}")
    print(f"Metrics saved to {METRICS_PATH}")
    print(f"Plots saved to {CONFUSION_MATRIX_PATH} and {ROC_CURVE_PATH}")


if __name__ == "__main__":
    main()
