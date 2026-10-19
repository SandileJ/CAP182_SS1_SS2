# STADIOchoice — STADIOstream Churn: Data Extract

STADIOstream households only — the satellite subscriber base and advertising logs are excluded as requested. Extract date is **2026-08-31**; subscriptions start from June 2022. `household_id` joins every table. `monthly_price` is in **cents**. Dates are `yyyy-MM-dd`, datetimes `yyyy-MM-dd HH:mm:ss`.

## Files

### `table1_subscription_billing.csv`
One row per household — plan, billing, tenure and churn status.  
Rows: 4,485

| Column | Description |
|---|---|
| `household_id` | String |
| `subscription_start_date` | Date |
| `plan_tier` | Categorical |
| `monthly_price` | Integer |
| `billing_cycle_date` | Date |
| `payment_method` | Categorical |
| `payment_status` | Categorical |
| `payment_failures_last_90_days` | Integer |
| `tenure_months` | Integer |
| `upgrade_downgrade_flag` | Categorical |
| `is_active` | Boolean |
| `churn_date` | Date |

### `table2_viewing_logs.csv`
Streaming event log. Sampled, not the complete event stream.  
Rows: 44,525

| Column | Description |
|---|---|
| `household_id` | String |
| `device_id` | String |
| `event_timestamp` | Datetime |
| `event_type` | Categorical |
| `title_id` | String |
| `watch_duration_seconds` | Integer |
| `device_type` | Categorical |

### `table3_cancellation_retention.csv`
Cancellation requests, retention offers and win-back outcomes.  
Rows: 988

| Column | Description |
|---|---|
| `household_id` | String |
| `cancel_request_date` | Date |
| `cancel_reason_code` | Categorical |
| `retention_offer_made` | Boolean |
| `retention_offer_type` | Categorical |
| `retention_offer_accepted` | Boolean |
| `win_back_outcome` | Categorical |

### `table4_customer_support.csv`
Support contacts with structured reason and raw agent notes.  
Rows: 3,149

| Column | Description |
|---|---|
| `household_id` | String |
| `contact_date` | Datetime |
| `contact_channel` | Categorical |
| `reason_code` | Categorical |
| `free_text_notes` | String |
| `resolution_status` | Categorical |

### `table5_content_catalogue.csv`
Title catalogue with genre, sport flag and licensing window.  
Rows: 640

| Column | Description |
|---|---|
| `title_id` | String |
| `title_name` | String |
| `genre` | Categorical |
| `is_sports_content` | Boolean |
| `licensing_window_start` | Date |
| `licensing_window_end` | Date |

### `table6_search_queries.csv`
Raw search terms and result counts. Zero results flags unmet demand.  
Rows: 13,587

| Column | Description |
|---|---|
| `household_id` | String |
| `search_timestamp` | Datetime |
| `search_term` | String |
| `result_count` | Integer |

## Data quality notes

This is an extract from live operational systems and has **not** been cleaned. Expect:

- Missing values in optional / conditionally-populated fields
- Inconsistent casing and stray whitespace in some free-text and categorical fields
- A small number of duplicate records
- Occasional out-of-range or implausible values from data-capture errors
- Some date fields captured in inconsistent formats

**Target:** `is_active` = FALSE (equivalently, `churn_date` populated) in `table1_subscription_billing.csv`.

**Leakage warning:** `churn_date`, `tenure_months` (measured to churn for churned households) and the whole of `table3_cancellation_retention.csv` are post-outcome. Note that households who were offered retention and accepted appear in Table 3 but are still active in Table 1 — those rows are the useful counterfactual, not an error.

**Notes**
- `watch_duration_seconds` and `title_id` are blank for Search, Scroll and other non-content events, as specified.
- `result_count = 0` in Table 6 marks a search that returned nothing — a direct measure of unmet content demand and a documented churn precursor.
- `free_text_notes` in Table 4 is raw agent text, intended for the text-mining component.
- Table 2 is a **sampled** event log rather than the complete stream, so per-household event counts are proportional to real activity but not absolute.

_Synthetic data supplied for the CAP182 capstone project. Not real client data._