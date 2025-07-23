import pandas as pd
import os

DATA_PATH = os.path.join("data", "revenue.csv")

def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Revenue dataset not found at {DATA_PATH}")
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    df["dayofyear"] = df["date"].dt.dayofyear
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
