# Mutual Fund Analytics

## Project Overview

This project focuses on analyzing mutual fund industry data using Python, Pandas, APIs, and data analytics techniques. The objective is to study fund performance, NAV trends, investor behavior, portfolio holdings, AUM growth, SIP inflows, and benchmark comparisons.

## Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
├── scripts/
│
├── requirements.txt
└── README.md
```

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

## Day 1 Activities

- Created project folder structure
- Configured Git and GitHub repository
- Installed project dependencies
- Loaded and explored all 10 datasets using Pandas
- Performed data quality checks
- Fetched live NAV data using MFAPI
- Retrieved NAV data for key mutual fund schemes
- Explored fund master dataset
- Validated AMFI codes against NAV history
- Generated data quality summary report

## Key Findings

- Total Mutual Fund Schemes: 40
- Total Fund Houses: 10
- Categories: Equity and Debt
- Sub-Categories: 12
- All AMFI codes successfully validated
- Only one dataset contained expected missing values in YoY growth percentage

## Technologies Used

- Python
- Pandas
- NumPy
- Requests
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook
- Git & GitHub

## Future Scope

- Fund performance analysis
- Risk-return analysis
- Benchmark comparison
- Investor behavior analysis
- Interactive dashboard development
- Portfolio analytics and insights
