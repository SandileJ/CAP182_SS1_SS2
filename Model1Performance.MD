# Model 1 Performance: Logistic Regression

Results of evaluating the Logistic Regression model on the held-out test set (1,409 customers).

## Metrics

| Metric | Value |
| --- | --- |
| Accuracy | 0.734 |
| Precision | 0.499 |
| Recall | 0.794 |
| F1 score | 0.613 |
| ROC-AUC | 0.842 |
| ROC-AUC 95% confidence interval | 0.821 to 0.863 |

The ROC-AUC confidence interval is estimated with 1,000 bootstrap resamples of the test set, as a statistical measure of how stable that estimate is rather than relying on a single point value.

Recall (0.794) is notably higher than precision (0.499), which is the expected effect of `class_weight="balanced"`: the model is deliberately biased toward catching churners, even at the cost of some false alarms, which fits a retention use case where missing an at-risk customer is more costly than an unnecessary offer.

## Files

- `scripts/model1_performance.py` (entry point, run this one)
- `scripts/metrics_utils.py` (shared metric and plotting helpers, imported by the script above, not run directly)

## How to use it

Run after `model1_logistic_regression.py` has produced `datasets/processed/model1_predictions.csv`:

```
python scripts/model1_performance.py
```

Writes `experimental_results/model1_metrics.json`, `experimental_results/model1_confusion_matrix.png`, and `experimental_results/model1_roc_curve.png`.
