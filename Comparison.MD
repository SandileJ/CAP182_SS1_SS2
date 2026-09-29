# Comparison: Model 1 vs Model 2

Both models were trained on the same feature set and evaluated on the same held-out test set (1,409 customers), so the comparison below is apples to apples.

## Metrics side by side

| Metric | Model 1: Logistic Regression | Model 2: XGBoost |
| --- | --- | --- |
| Accuracy | 0.734 | 0.753 |
| Precision | 0.499 | 0.523 |
| Recall | 0.794 | 0.802 |
| F1 score | 0.613 | 0.633 |
| ROC-AUC | 0.842 | 0.844 |

XGBoost is ahead on every single metric, though the ROC-AUC gap (0.842 vs 0.844) is small and sits well within both models' overlapping 95% confidence intervals from Part C's individual evaluations, so on ranking ability alone the two are close.

## Is the difference statistically significant?

Point metrics alone do not say whether XGBoost is meaningfully better or just noisier on this particular test set, so an exact McNemar's test was run on the paired predictions (same customers, both models), which is the right test here because both models are scored on the same test set rather than independent samples.

| | Value |
| --- | --- |
| Customers Model 1 got wrong but Model 2 got right | 66 |
| Customers Model 1 got right but Model 2 got wrong | 39 |
| p-value | 0.0108 |
| Statistically significant at 0.05 | Yes |

A p-value of 0.0108 means the two models disagree on enough customers, and in a consistent enough direction, that the difference is unlikely to be chance. XGBoost is the statistically better classifier on this dataset, not just numerically higher by a rounding margin.

## Files

- `scripts/comparison.py` (entry point, run this one)
- `scripts/metrics_utils.py` (shared metric and plotting helpers, imported by the script above, not run directly)

## How to use it

Run after both `model1_logistic_regression.py` and `model2_xgboost.py` have produced their prediction files:

```
python scripts/comparison.py
```

Writes `experimental_results/comparison_metrics.csv`, `experimental_results/mcnemar_test.json`, and `experimental_results/roc_curve_comparison.png`.
