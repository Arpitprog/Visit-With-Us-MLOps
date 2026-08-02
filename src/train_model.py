import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv("train.csv")

X = train.drop("ProdTaken", axis=1)
y = train["ProdTaken"]

cat = X.select_dtypes(include="object").columns
num = X.select_dtypes(exclude="object").columns

preprocessor = ColumnTransformer(
    [
        (
            "num",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median"))
                ]
            ),
            num
        ),
        (
            "cat",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("encoder", OneHotEncoder(handle_unknown="ignore"))
                ]
            ),
            cat
        )
    ]
)

pipeline = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(random_state=42))
    ]
)

pipeline.fit(X, y)

joblib.dump(pipeline, "model.pkl")

print("Model saved successfully.")
