from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
from sqlalchemy import select, func
from .db import engine
from .models import transactions
from .analytics import (
    get_revenue_insights,
    get_retention_insights,
    get_transaction_summary,
    get_customer_segments,
)

app = FastAPI(title="Analytics API")


class KPIResponse(BaseModel):
    total_revenue: float
    total_transactions: int
    unique_customers: int
    average_order_value: float


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/kpis", response_model=KPIResponse)
def get_kpis():
    with engine.connect() as conn:
        stmt = select(
            func.sum(transactions.c.amount).label("total_revenue"),
            func.count().label("total_transactions"),
            func.count(func.distinct(transactions.c.customer_id)).label("unique_customers"),
            func.avg(transactions.c.amount).label("average_order_value"),
        )
        row = conn.execute(stmt).one()

    if row.total_transactions == 0:
        raise HTTPException(status_code=404, detail="No transaction data available")

    return KPIResponse(
        total_revenue=float(row.total_revenue or 0),
        total_transactions=int(row.total_transactions or 0),
        unique_customers=int(row.unique_customers or 0),
        average_order_value=float(row.average_order_value or 0),
    )


@app.get("/kpis/revenue")
def revenue_kpis():
    return get_revenue_insights()


@app.get("/kpis/retention")
def retention_kpis():
    return get_retention_insights()


@app.get("/kpis/transactions")
def transactions_kpis():
    return get_transaction_summary()


@app.get("/analytics/customer-segments")
def customer_segments():
    return get_customer_segments()


@app.get("/transactions/by-date")
def transactions_by_date(start_date: date, end_date: date):
    with engine.connect() as conn:
        stmt = (
            select(
                transactions.c.transaction_date,
                func.sum(transactions.c.amount).label("revenue"),
                func.count().label("transaction_count"),
            )
            .where(transactions.c.transaction_date.between(start_date, end_date))
            .group_by(transactions.c.transaction_date)
            .order_by(transactions.c.transaction_date)
        )
        results = conn.execute(stmt).all()

    return [
        {
            "date": row.transaction_date.date().isoformat(),
            "revenue": float(row.revenue),
            "transaction_count": int(row.transaction_count),
        }
        for row in results
    ]
