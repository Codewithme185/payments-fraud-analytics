# Payments Fraud Analytics Dashboard

## Overview

A data analytics project for exploring payment transactions and
identifying patterns associated with fraudulent activity. The workflow
uses Python and SQL for data preparation and analysis, with Tableau for
dashboard-based reporting.

## Objectives

-   Explore transaction-level payment data.
-   Compare transaction patterns and identify suspicious behaviour.
-   Summarize key findings with charts and an interactive Tableau
    dashboard.
-   Support data-driven fraud monitoring and investigation.

## Tools & Technologies

-   Python
-   Pandas
-   SQL / SQLite
-   Tableau
-   Data visualization

## Dataset

The project was developed using a large transaction dataset with
approximately 6.36 million rows and 11 columns.

The raw CSV and SQLite database are excluded from this repository
because of their size. Obtain the dataset from its original authorized
source and place the CSV in the project folder before running the
analysis.

Expected CSV filename: `PS_20174392719_1491204439457_log.csv`

## Project Workflow

1.  Load and inspect transaction data.
2.  Clean and prepare data for analysis.
3.  Use SQL/Python to summarize transaction behaviour.
4.  Create visualizations for key patterns.
5.  Present findings in Tableau.

## How to Run

1.  Clone or download this repository.

2.  Install the required Python packages used by your analysis scripts,
    for example:

    ``` bash
    python3 -m pip install pandas matplotlib
    ```

3.  Place the source CSV in the project folder.

4.  Run the Python analysis script available in the project, if
    included.

5.  Open the Tableau workbook/dashboard in Tableau Desktop.

> Note: Update package installation commands to match the imports in
> your final Python script. Tableau workbooks may require the source
> data connection to be relinked locally.

## Limitations

This project supports analytical review; a flagged transaction should
not automatically be treated as confirmed fraud. Findings depend on the
source dataset and analysis assumptions.

## Author

Codewithme185
