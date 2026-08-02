import pandas as pd

df = pd.read_csv("data/tourism.csv")

print("="*50)
print("DATA VALIDATION")
print("="*50)

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nSummary:")
print(df.describe(include="all"))
