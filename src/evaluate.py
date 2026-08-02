import pandas as pd
import joblib

from sklearn.metrics import accuracy_score

test = pd.read_csv("test.csv")

X = test.drop("ProdTaken", axis=1)
y = test["ProdTaken"]

model = joblib.load("model.pkl")

pred = model.predict(X)

accuracy = accuracy_score(y, pred)

print("Accuracy:", accuracy)
