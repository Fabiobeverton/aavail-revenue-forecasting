import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Constants
START_DATE = datetime(2023, 1, 1)
NUM_DAYS = 500
COUNTRIES = ["USA", "EIRE", "Germany", "Singapore"]
REVENUE_MIN = 8000
REVENUE_MAX = 15000
OUTPUT_DIR = "data"
OUTPUT_FILE = "revenue.csv"

def generate_revenue_data():
    records = []

    for i in range(NUM_DAYS):
        date = START_DATE + timedelta(days=i)
        for country in COUNTRIES:
            revenue = round(random.uniform(REVENUE_MIN, REVENUE_MAX), 2)
            records.append({
                "date": date.strftime("%Y-%m-%d"),
                "country": country,
                "revenue": revenue
            })

    df = pd.DataFrame(records)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    df.to_csv(output_path, index=False)

    print(f"[✔] Revenue data saved to: {output_path}")
    print(df.head())

if __name__ == "__main__":
    generate_revenue_data()
