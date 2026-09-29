# Model 2 Performance: XGBoost

Results of evaluating the XGBoost model on the same held-out test set (1,409 customers) as Model 1.

## Metrics

| Metric | Value |
| --- | --- |
| Accuracy | 0.753 |
| Precision | 0.523 |
| Recall | 0.802 |
| F1 score | 0.633 |
| ROC-AUC | 0.844 |
| ROC-AUC 95% confidence interval | 0.821 to 0.865 |

The ROC-AUC confidence interval is estimated with 1,000 bootstrap resamples of the test set, the same method used for Model 1, so the two are directly comparable.

XGBoost improves on every metric compared to Model 1, most noticeably precision (0.523 vs 0.499) while keeping recall roughly the same (0.802 vs 0.794), meaning it catches a similar share of churners with fewer false alarms.

## Files

- `scripts/model2_performance.py` (entry point, run this one)
- `scripts/metrics_utils.py` (shared metric and plotting helpers, imported by the script above, not run directly)

## How to use it

Run after `model2_xgboost.py` has produced `datasets/processed/model2_predictions.csv`:

```
python scripts/model2_performance.py
```

Writes `experimental_results/model2_metrics.json`, `experimental_results/model2_confusion_matrix.png`, and `experimental_results/model2_roc_curve.png`.
