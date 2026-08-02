import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/tourism.csv")

df = df.drop(columns=["Unnamed: 0", "CustomerID"])

train, test = train_test_split(
    df,
    test_size=0.20,
    random_state=42,
    stratify=df["ProdTaken"]
)

train.to_csv("train.csv", index=False)
test.to_csv("test.csv", index=False)

print("Train and Test datasets created successfully.")
