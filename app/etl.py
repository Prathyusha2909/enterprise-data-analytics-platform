import pandas as pd
from pathlib import Path
from sqlalchemy import insert
from .db import engine
from .models import transactions

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def load_raw_data(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    expected = [
        "transaction_id",
        "transaction_date",
        "customer_id",
        "amount",
        "product_category",
        "business_unit",
        "status",
    ]
    if not set(expected).issubset(df.columns):
        raise ValueError("Raw file missing required columns")

    df = df[expected].copy()
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["transaction_id", "transaction_date", "customer_id", "amount"])
    df = df[df["amount"] >= 0]
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["product_category"] = df["product_category"].fillna("Unknown")
    df["business_unit"] = df["business_unit"].fillna("General")
    df["status"] = df["status"].fillna("Completed")
    return df


def load_to_postgres(df: pd.DataFrame) -> int:
    records = df.to_dict(orient="records")
    with engine.begin() as conn:
        stmt = insert(transactions).on_conflict_do_nothing(index_elements=[transactions.c.transaction_id])
        result = conn.execute(stmt, records)
        return result.rowcount


def run_etl() -> None:
    raw_files = sorted(RAW_DIR.glob("*.csv"))
    if not raw_files:
        print("No raw CSV files found in data/raw/")
        return

    total_loaded = 0
    for raw_file in raw_files:
        print(f"Processing {raw_file.name}")
        df = load_raw_data(raw_file)
        df = transform_data(df)
        loaded = load_to_postgres(df)
        total_loaded += loaded
        print(f"Loaded {loaded} records from {raw_file.name}")

    print(f"ETL complete. Total records loaded: {total_loaded}")


if __name__ == "__main__":
    run_etl()
