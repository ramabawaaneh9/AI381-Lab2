
NUMERIC = [
    "tenure_months",
    "monthly_fee",
    "support_calls",
]

CATEGORICAL = [
    "contract",
    "internet_service",
]

FEATURES = NUMERIC + CATEGORICAL
TARGET = "churn"


def validate(df):
    required = FEATURES + [TARGET]
    missing = [column for column in required if column not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df

