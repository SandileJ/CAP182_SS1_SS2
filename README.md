# CAP182 SS1: Predicting and Preventing Streaming Churn at STADIOchoice

Client: STADIOchoice
Module: CAP182 Capstone, SS1

## Repository Structure

| Folder | Purpose |
| --- | --- |
| `datasets/raw` | Original, unmodified data as received from the client. Ignored by git, tracked by data version and a data dictionary instead, since this data is client confidential. |
| `datasets/processed` | Cleaned, joined, and feature engineered datasets derived from the raw data, ready for modelling. |
| `models` | Trained model artifacts, model configuration files, and model evaluation summaries. |
| `experimental_setup` | Notebooks and scripts that define each experiment, including feature sets, train and test splits, and hyperparameters used. |
| `experimental_results` | Output of each experiment run, including metrics, logs, and saved comparisons between experiments. |
| `scripts/statistical_helpers` | Reusable helper functions for statistical tests, data validation, and model comparison. |
| `scripts/visualisation` | Reusable plotting and dashboard scripts used across the project. |
| `reports` | Standalone written deliverables for the client, including the Data Request PDF. |

## Motivation

STADIOchoice knows it has a churn problem. It says so itself: streaming monthly churn has climbed from 6.5% to 9.2% in two years, and the cost of winning a new streaming subscriber has gone up by almost 50% over the same stretch, from R240 to R355. What the business doesn't have is a way to tell, ahead of time, which subscribers are actually at risk of leaving.

That gap shows up in a pretty telling way. Right now, anyone who clicks cancel gets a retention offer, a discount, a free month, whatever it takes. It sounds generous, but it's actually a blunt instrument. A lot of that spend goes to people who were never going to leave in the first place, while the subscribers who quietly stop watching and just let their subscription lapse never get flagged at all. STADIOchoice is spending real money rescuing subscribers it didn't need to rescue, and missing the ones it should be worried about.

This matters because retention is literally the first line item in the company's own 2030 strategy: "win the streaming war on retention, not just sign-ups." That's not a throwaway line, it's a direct admission that the current approach isn't working well enough. And the timing is good, because for the first time STADIOchoice has a unified data platform that joins viewing behaviour, billing, cancellations and support history for the same household, going back three to five years depending on the source. The pieces needed to actually solve this are sitting there, just not connected yet.

That's what this project is for: turning STADIOchoice's reactive, one-size-fits-all retention process into something that can spot a household drifting toward cancellation early, and put the retention spend where it will actually change the outcome instead of where it's easiest to react.

## Problem Statement

Section in progress.

## Data Request

See `reports/` for the full Data Request document.

## RAAIDD Log

Section in progress.
