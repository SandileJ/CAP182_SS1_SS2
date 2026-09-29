"""Shared metric and plotting helpers used by model1_performance.py,
model2_performance.py, and comparison.py. Not a standalone deliverable
on its own, imported by those three scripts.
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)


def compute_metrics(y_true, y_pred, y_proba) -> dict:
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
        "roc_auc": roc_auc_score(y_true, y_proba),
    }


def bootstrap_ci(y_true, y_proba, metric_fn, n_boot: int = 1000, seed: int = 42):
    """95% confidence interval for a probability-based metric (e.g.
    ROC-AUC), estimated by resampling the test set with replacement.
    """
    rng = np.random.default_rng(seed)
    y_true = np.asarray(y_true)
    y_proba = np.asarray(y_proba)
    n = len(y_true)

    scores = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        sample_true = y_true[idx]
        if len(np.unique(sample_true)) < 2:
            continue
        scores.append(metric_fn(sample_true, y_proba[idx]))

    lower, upper = np.percentile(scores, [2.5, 97.5])
    return lower, upper


def plot_confusion_matrix(y_true, y_pred, title: str, out_path: str) -> None:
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(cm, cmap="Purples")
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["No churn", "Churn"])
    ax.set_yticklabels(["No churn", "Churn"])
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(title)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm[i, j], ha="center", va="center", color="black")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_roc_curves(curves: list[tuple[str, np.ndarray, np.ndarray]], out_path: str) -> None:
    """curves: list of (label, y_true, y_proba) tuples, one per model."""
    fig, ax = plt.subplots(figsize=(5, 5))
    for label, y_true, y_proba in curves:
        fpr, tpr, _ = roc_curve(y_true, y_proba)
        auc = roc_auc_score(y_true, y_proba)
        ax.plot(fpr, tpr, label=f"{label} (AUC={auc:.3f})")
    ax.plot([0, 1], [0, 1], linestyle="--", color="grey", label="Random")
    ax.set_xlabel("False positive rate")
    ax.set_ylabel("True positive rate")
    ax.set_title("ROC curve")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
