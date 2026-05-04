import pandas as pd
from sqlalchemy import create_engine

def load_bronze():
    data = [
        {"user_id": 1, "event_type": "purchase", "amount": 100},
        {"user_id": 1, "event_type": "purchase", "amount": 200},
        {"user_id": 2, "event_type": "purchase", "amount": 150},
        {"user_id": 3, "event_type": "click", "amount": 0}
    ]

    df = pd.DataFrame(data)

    engine = create_engine("postgresql://airflow:airflow@postgres:5432/warehouse")

    df.to_sql("raw_events", engine, if_exists="replace", index=False)