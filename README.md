# Payments Fraud Analytics Dashboard

## Overview

**Payments Fraud Analytics Dashboard** is a data analytics project focused on analyzing payment transactions and identifying patterns associated with potentially fraudulent activity.

The project combines Python, SQL, and Tableau to explore large-scale transaction data, calculate key fraud-related metrics, and present analytical findings through interactive dashboards.

It demonstrates practical skills in data cleaning, exploratory data analysis, SQL querying, KPI development, and business intelligence reporting.

## Project Objectives

- Analyze millions of payment transactions to understand transaction behavior.
- Compare fraudulent and legitimate transaction patterns.
- Calculate key performance indicators for fraud monitoring.
- Identify unusual transaction patterns for further investigation.
- Build visualizations and interactive Tableau dashboards.
- Support data-driven financial risk analysis and reporting.

## Tools & Technologies

- **Python:** Data processing and exploratory analysis.
- **Pandas:** Data manipulation and aggregation.
- **SQL / SQLite:** Transaction querying and analysis.
- **Tableau:** Interactive dashboards and data visualization.
- **Matplotlib:** Analytical charts and visualizations.

## Dataset

This project uses a large transaction dataset containing approximately **6.36 million rows and 11 columns**.

Expected source filename:

`PS_20174392719_1491204439457_log.csv`

The dataset includes transaction-related information such as transaction type, amount, account balances, and fraud labels.

**Dataset availability:** The raw CSV and SQLite database are excluded from this repository because of their size. Obtain the dataset from its original authorized source and place the CSV in the project directory before running the analysis.

## Project Workflow

1. **Data Loading:** Import the transaction dataset and inspect its structure.
2. **Data Cleaning:** Validate data types, check data quality, and prepare the data for analysis.
3. **Exploratory Data Analysis:** Examine transaction volumes, amounts, transaction types, and fraud patterns.
4. **SQL Analysis:** Query transaction records and calculate relevant analytical metrics.
5. **KPI Development:** Calculate fraud-related indicators to support monitoring.
6. **Data Visualization:** Create charts to communicate important findings.
7. **Dashboard Development:** Present the results through Tableau visualizations.

## Key Findings

The analysis identified the following result from the current project run:

| Metric | Result |
|---|---:|
| Total Transactions | 6,362,620 |
| Total Dataset Columns | 11 |
| Observed Fraud Rate | Approximately 0.13% |

The fraud rate represents the proportion of records labeled as fraudulent in the analyzed dataset. It is a dataset-specific result, not a measure of fraud prevalence across the entire payments industry.

## Dashboard Highlights

The Tableau dashboard supports analysis of:

- Overall transaction activity.
- Fraudulent versus non-fraudulent transactions.
- Fraud rates across transaction categories.
- Transaction amounts and account balance patterns.
- Key fraud monitoring metrics.

*The exact dashboard contents depend on the worksheets and visualizations included in the Tableau workbook.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Codewithme185/payments-fraud-analytics.git
cd payments-fraud-analytics
```

### 2. Install Dependencies

```bash
python3 -m pip install pandas matplotlib
```

Install any additional packages required by your scripts.

### 3. Add the Dataset

Place the source CSV file in the project directory:

```text
payments-fraud-analytics/
├── PS_20174392719_1491204439457_log.csv
├── analysis.py
├── dashboard.twb
└── README.md
```

*This is an illustrative structure. Use the actual script and workbook filenames from your repository.*

### 4. Run the Analysis

Run the Python analysis script included in your repository. For example:

```bash
python3 analysis.py
```

Replace `analysis.py` with the actual script filename.

### 5. Open the Tableau Dashboard

Open the Tableau workbook in Tableau Desktop. If Tableau cannot locate the source dataset, reconnect it to the CSV or database on your computer.

## Limitations

- The analysis depends on the source dataset and its fraud labels.
- A low fraud rate can make overall accuracy misleading when evaluating a fraud detection model.
- Unusual transaction patterns do not necessarily indicate confirmed fraud.
- Findings from this dataset may not generalize to real-world payment systems.
- This project is intended for analytical and educational purposes, not as a standalone fraud prevention system.

## Future Improvements

- Develop a machine learning model for transaction risk classification.
- Add precision, recall, F1-score, and ROC-AUC where applicable.
- Implement time-based fraud trend analysis.
- Optimize SQL queries for large transaction datasets.
- Add automated reporting and dashboard refresh workflows.
- Explore methods for handling class imbalance.
- Develop alerts for transactions requiring manual review.

## Skills Demonstrated

- Data cleaning and preprocessing.
- Exploratory data analysis.
- Python and Pandas.
- SQL-based analytical querying.
- KPI calculation and fraud-rate analysis.
- Tableau dashboard development.
- Financial data interpretation.
- Communicating analytical findings.

## Author

**Codewithme185**

GitHub: [@Codewithme185](https://github.com/Codewithme185)

---

*This project demonstrates transaction analytics and fraud-pattern exploration for educational and portfolio purposes. A flagged transaction is not proof of fraud.*
