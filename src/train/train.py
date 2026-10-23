import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA = "churn_v2.csv"

numeric = [
    "tenure_months",
    "monthly_fee",
    "support_calls",
]

categorical = [
    "contract",
    "internet_service",
]


def train():
    df = pd.read_csv(DATA)

    X = df[numeric + categorical]
    y = df["churn"]

    X_train, _, y_train, _ = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = Pipeline([
        (
            "prep",
            ColumnTransformer([
                ("num", StandardScaler(), numeric),
                ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
            ]),
        ),
        ("clf", LogisticRegression(max_iter=1000)),
    ])

    model.fit(X_train, y_train)

    joblib.dump(model, "model.joblib")

    print("Model trained and saved as model.joblib")


if __name__ == "__main__":
    train()