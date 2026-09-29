# CAP182 Capstone: Predicting and Preventing Streaming Churn at STADIOchoice

Client: STADIOchoice, used for every submission in this module.
Module: CAP182 Capstone
Submissions in this repository: SS1, SS2

STADIOchoice is not yet ready to share its sensitive subscriber data, so before that data arrives, SS2 proves the churn prediction approach on a public dataset (Telco Customer Churn) as a stand in. Everything for both submissions lives in this one repository, this project does not switch client or repository between submissions.

## Repository Structure

| Folder | Purpose |
| --- | --- |
| `datasets/raw` | Original, unmodified data. For STADIOchoice's own data this is client confidential and ignored by git, tracked by a data dictionary instead. The public Telco Customer Churn dataset used for SS2 is tracked directly here, since it carries no confidentiality restriction. |
| `datasets/processed` | Cleaned, joined, and feature engineered datasets derived from the raw data, ready for modelling, plus the train/test splits and model prediction outputs produced by the SS2 scripts. |
| `models` | Trained model artifacts (`.joblib`) and the fitted feature scaler. |
| `experimental_setup` | Reserved for future experiment definitions. SS2's experiment setup (feature sets, train/test splits, hyperparameters) currently lives directly in `scripts/`, see the Part B section below. |
| `experimental_results` | Output of each experiment run: metrics, statistical test results, and plots. |
| `scripts` | Preprocessing, feature engineering, model, and performance scripts. |
| `reports` | Standalone PDF deliverables: SS1's Data Request, SS2's related work and data description report, and SS2's recommendations report. |

## SS1

### Motivation

STADIOchoice knows it has a churn problem. It says so itself: streaming monthly churn has climbed from 6.5% to 9.2% in two years, and the cost of winning a new streaming subscriber has gone up by almost 50% over the same stretch, from R240 to R355. What the business doesn't have is a way to tell, ahead of time, which subscribers are actually at risk of leaving.

That gap shows up in a pretty telling way. Right now, anyone who clicks cancel gets a retention offer, a discount, a free month, whatever it takes. It sounds generous, but it's actually a blunt instrument. A lot of that spend goes to people who were never going to leave in the first place, while the subscribers who quietly stop watching and just let their subscription lapse never get flagged at all. STADIOchoice is spending real money rescuing subscribers it didn't need to rescue, and missing the ones it should be worried about.

This matters because retention is literally the first line item in the company's own 2030 strategy: "win the streaming war on retention, not just sign-ups." That's not a throwaway line, it's a direct admission that the current approach isn't working well enough. And the timing is good, because for the first time STADIOchoice has a unified data platform that joins viewing behaviour, billing, cancellations and support history for the same household, going back three to five years depending on the source. The pieces needed to actually solve this are sitting there, just not connected yet.

That's what this project is for: turning STADIOchoice's reactive, one-size-fits-all retention process into something that can spot a household drifting toward cancellation early, and put the retention spend where it will actually change the outcome instead of where it's easiest to react.

### Problem Statement

STADIOchoice cannot currently identify, ahead of time, which STADIOstream households are likely to cancel their subscription in the near term. As a result, retention offers are applied reactively and indiscriminately at the point of cancellation, rather than proactively to the households most at risk. This drives two costs at once: wasted retention spend on subscribers who would have stayed regardless, and unrecovered revenue from subscribers who churn silently without ever triggering the existing offer process.

This is a data science problem because STADIOchoice already collects the behavioural, billing, and support signals needed to characterise churn risk before it happens, spread across streaming viewing logs, subscription and billing history, past cancellation and win-back outcomes, and customer support contacts. What is missing is a model that turns those historical patterns into a forward-looking churn risk score per household, so that retention action can be targeted rather than blanket. The project scope is to build and evaluate such a model, and to translate its output into a ranked, actionable list of at-risk households that STADIOchoice's retention process can use.

### Data Request

See `reports/STADIOchoice_Data_Request.pdf` for the full Data Request document.

### RAAIDD Log

| RAAIDD | Description |
| --- | --- |
| Risks | Satellite side viewing data is thin, so households that use both satellite and streaming may be hard to model well.<br>Some behavioural logs are sampled rather than complete, which could bias the model if the sampling isn't even across subscriber groups.<br>Churn is a minority event (around 9.2% monthly), so the model could end up biased toward predicting "will not churn" unless this is handled deliberately.<br>Churn drivers tied to specific events, like a tournament ending, may shift over time and make the model less accurate the further it gets from its training period.<br>Subscriber viewing, billing, and support data is sensitive, so mishandling it would breach STADIOchoice's trust and possibly data protection obligations. |
| Actions | Submit the Part C data request to STADIOchoice and follow up on any fields that come back incomplete or unclear.<br>Run exploratory analysis on every data source to check quality, coverage, and time range before any modelling starts.<br>Agree a precise definition of "churn" with STADIOchoice (full cancellation versus a pause or downgrade) before building the target variable.<br>Build a simple baseline model first, then compare more complex models against it using the statistical helper scripts.<br>Set up a time based train and test split, training on older data and testing on more recent data, so the model isn't evaluated on data from the same period it learned from. |
| Assumptions | STADIOchoice can provide a consistent household level identifier across all data sources.<br>STADIOchoice's definition of churn for streaming subscribers is a full cancellation, not a pause or downgrade.<br>The three years of streaming viewing history described in the briefing pack will be provided in full, not as a partial sample.<br>Past retention offer and win-back outcomes have been logged consistently enough over time to be usable, not just for evaluation but potentially as a model input. |
| Issues | No issues have come up yet, since the project is still at the proposal and data request stage. This section will be updated once data is received and modelling work begins. |
| Decisions | Scoped the project to STADIOstream churn only, excluding the satellite subscriber base, since satellite has little viewing detail and would need its own churn definition entirely.<br>Chose to frame this as a supervised churn risk score per household rather than general audience segmentation, since STADIOchoice's actual need is prioritising who to contact, not just understanding groups. |
| Dependencies | Feature engineering depends on STADIOchoice fulfilling the Part C data request.<br>Defining the churn label depends on STADIOchoice confirming what counts as churn versus a pause or downgrade.<br>The time based validation split depends on having enough distinct historical periods in the delivered data to split on.<br>Using customer support free text as a model feature depends on first confirming there's no restriction on using that content for this purpose. |

## SS2

STADIOchoice is not yet ready to share its own data (see SS1's Data Request above), so SS2 proves the churn prediction approach on the Telco Customer Churn dataset, a public dataset covering the same kind of problem, before that real data arrives.

Run `pip install -r requirements.txt` before running any SS2 script.

### Related Work and Data Description

See `reports/Related_Work_And_Data_Description.pdf`.

### Modelling

- [Preprocessing.MD](Preprocessing.MD)
- [FeatureEngineering.MD](FeatureEngineering.MD)
- [Model1.MD](Model1.MD)
- [Model2.MD](Model2.MD)

### Results and Findings

- [Model1Performance.MD](Model1Performance.MD)
- [Model2Performance.MD](Model2Performance.MD)
- [Comparison.MD](Comparison.MD)

### Recommendations

See `reports/Recommendations.pdf`.
