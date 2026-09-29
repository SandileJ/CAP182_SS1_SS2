"""Compares Model 1 (Logistic Regression) and Model 2 (XGBoost) on the
same held-out test set: a side-by-side metrics table, a combined ROC
curve, and an exact McNemar's test to check whether the difference in
errors between the two models is statistically significant, rather
than relying on point metrics alone.
"""

import json

import pandas as pd
from scipy.stats import binomtest

from metrics_utils import compute_metrics, plot_roc_curves

MODEL1_PREDICTIONS_PATH = "datasets/processed/model1_predictions.csv"
MODEL2_PREDICTIONS_PATH = "datasets/processed/model2_predictions.csv"
COMPARISON_TABLE_PATH = "experimental_results/comparison_metrics.csv"
MCNEMAR_PATH = "experimental_results/mcnemar_test.json"
ROC_CURVE_PATH = "experimental_results/roc_curve_comparison.png"


def mcnemar_exact_test(y_true, y_pred_1, y_pred_2) -> dict:
    correct_1 = y_pred_1 == y_true
    correct_2 = y_pred_2 == y_true

    # n_01: Model 1 wrong, Model 2 right. n_10: Model 1 right, Model 2 wrong.
    n_01 = int(((~correct_1) & correct_2).sum())
    n_10 = int((correct_1 & (~correct_2)).sum())

    n_discordant = n_01 + n_10
    if n_discordant == 0:
        p_value = 1.0
    else:
        result = binomtest(min(n_01, n_10), n_discordant, 0.5, alternative="two-sided")
        p_value = float(result.pvalue)

    return {
        "model1_wrong_model2_right": n_01,
        "model1_right_model2_wrong": n_10,
        "p_value": p_value,
        "significant_at_0.05": bool(p_value < 0.05),
    }


def main() -> None:
    p1 = pd.read_csv(MODEL1_PREDICTIONS_PATH)
    p2 = pd.read_csv(MODEL2_PREDICTIONS_PATH)

    assert (p1["y_true"] == p2["y_true"]).all(), "Test sets must match to compare models fairly"
    y_true = p1["y_true"]

    metrics_1 = compute_metrics(y_true, p1["y_pred"], p1["y_proba"])
    metrics_2 = compute_metrics(y_true, p2["y_pred"], p2["y_proba"])

    comparison = pd.DataFrame(
        {"Model 1: Logistic Regression": metrics_1, "Model 2: XGBoost": metrics_2}
    )
    comparison.to_csv(COMPARISON_TABLE_PATH)

    mcnemar_result = mcnemar_exact_test(y_true, p1["y_pred"], p2["y_pred"])
    with open(MCNEMAR_PATH, "w") as f:
        json.dump(mcnemar_result, f, indent=2)

    plot_roc_curves(
        [
            ("Model 1: Logistic Regression", y_true, p1["y_proba"]),
            ("Model 2: XGBoost", y_true, p2["y_proba"]),
        ],
        ROC_CURVE_PATH,
    )

    print("Metrics comparison:")
    print(comparison)
    print()
    print("McNemar's exact test (are the two models' errors significantly different?):")
    for key, value in mcnemar_result.items():
        print(f"  {key}: {value}")
    print()
    print(f"Comparison table saved to {COMPARISON_TABLE_PATH}")
    print(f"McNemar's test result saved to {MCNEMAR_PATH}")
    print(f"Combined ROC curve saved to {ROC_CURVE_PATH}")


if __name__ == "__main__":
    main()
