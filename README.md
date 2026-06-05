# Mutual Fund Analytics

## Project Overview

This project focuses on analyzing mutual fund industry data using Python, SQL, APIs, and data analytics techniques. The objective is to build an end-to-end mutual fund analytics platform covering data ingestion, cleaning, database management, exploratory data analysis, performance analytics, and dashboard development.

---

## Project Structure

```text
MutualFundAnalytics/
│
├── charts/
├── dashboard/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   └── 03_EDA_Analysis.ipynb
│
├── reports/
├── scripts/
├── sql/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Datasets Used

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Day 1 – Data Ingestion & Validation

### Activities Completed

* Created project folder structure
* Configured Git and GitHub repository
* Installed project dependencies
* Loaded and explored all 10 datasets using Pandas
* Performed data quality checks
* Fetched live NAV data using MFAPI
* Retrieved NAV data for selected mutual fund schemes
* Explored fund master dataset
* Validated AMFI codes against NAV history
* Generated data quality summary report

### Key Findings

* Total Mutual Fund Schemes: 40
* Total Fund Houses: 10
* Categories: Equity and Debt
* Sub-Categories: 12
* All AMFI codes successfully validated

---

## Day 2 – Data Cleaning & Database Development

### Activities Completed

* Cleaned NAV history data
* Cleaned investor transaction data
* Cleaned scheme performance data
* Created processed datasets
* Designed SQLite star schema
* Developed SQL scripts
* Created data dictionary
* Prepared database loading scripts

### Deliverables

* Cleaned datasets in `data/processed`
* SQLite database structure
* SQL schema design
* Analytical SQL queries
* Data dictionary documentation

---

## Day 3 – Exploratory Data Analysis (EDA)

### Analyses Performed

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Inflow Trend Analysis
* Category Inflow Heatmap
* Investor Demographics Analysis
* Geographic Distribution Analysis
* Folio Growth Analysis
* NAV Correlation Analysis
* Sector Allocation Analysis
* Risk vs Return Analysis

### Visualizations Created

* NAV Trend Charts
* AUM Growth Charts
* SIP Trend Charts
* Category Heatmaps
* Age Distribution Charts
* Gender Distribution Charts
* Geographic Analysis Charts
* Correlation Matrix
* Sector Allocation Donut Chart
* Risk and Return Visualizations

### Key Insights

1. Mutual fund NAVs showed a strong upward trend over time.
2. SBI Mutual Fund maintained the highest AUM.
3. SIP inflows reached record highs during the analysis period.
4. Flexi Cap and Large Cap categories attracted strong inflows.
5. Investors aged 26–45 formed the largest investor group.
6. T30 cities contributed the majority of investments.
7. Industry folio count increased significantly.
8. Large-cap funds exhibited strong positive correlations.
9. Financial Services and IT sectors dominated allocations.
10. Higher returns were generally associated with higher volatility.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* SQLite
* SQLAlchemy
* Matplotlib
* Seaborn
* Plotly
* Jupyter Notebook
* Git & GitHub

---

## Current Project Status

### Completed

* Day 1: Data Ingestion & Validation
* Day 2: Data Cleaning & Database Design
* Day 3: Exploratory Data Analysis

### Upcoming

* Day 4: Performance Analytics
* Day 5: Dashboard Development
* Day 6: Advanced Analytics
* Day 7: Final Report & Presentation

---

## Author

Sai Teja Reddy Tellapally

Mutual Fund Analytics Capstone Project
