import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

print("\nTotal Schemes:")
print(len(df))

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].value_counts())

print("\nPlans:")
print(df["plan"].unique())