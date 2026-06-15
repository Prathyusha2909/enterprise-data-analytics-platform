from sqlalchemy import select, func, case
from .db import engine
from .models import transactions


def get_kpi_summary():
    with engine.connect() as conn:
        stmt = select(
            func.sum(transactions.c.amount).label("total_revenue"),
            func.count().label("total_transactions"),
            func.count(func.distinct(transactions.c.customer_id)).label("unique_customers"),
            func.avg(transactions.c.amount).label("average_order_value"),
        )
        return conn.execute(stmt).one()


def get_revenue_insights():
    with engine.connect() as conn:
        stmt = select(
            func.sum(transactions.c.amount).label("total_revenue"),
        )
        total_row = conn.execute(stmt).one()

        monthly_stmt = (
            select(
                func.date_trunc("month", transactions.c.transaction_date).label("month"),
                func.sum(transactions.c.amount).label("monthly_revenue"),
            )
            .group_by(func.date_trunc("month", transactions.c.transaction_date))
            .order_by(func.date_trunc("month", transactions.c.transaction_date))
        )
        monthly_rows = conn.execute(monthly_stmt).all()

    monthly_growth = 0.0
    if len(monthly_rows) >= 2:
        current = float(monthly_rows[-1].monthly_revenue or 0)
        prior = float(monthly_rows[-2].monthly_revenue or 0)
        if prior != 0:
            monthly_growth = (current - prior) / prior * 100

    return {
        "total_revenue": float(total_row.total_revenue or 0),
        "monthly_revenue_growth": round(monthly_growth, 2),
    }


def get_retention_insights():
    with engine.connect() as conn:
        customer_counts = (
            select(
                transactions.c.customer_id,
                func.count().label("transaction_count"),
            )
            .group_by(transactions.c.customer_id)
            .subquery()
        )

        total_customers_stmt = select(func.count()).select_from(customer_counts)
        repeat_customers_stmt = select(func.count()).select_from(customer_counts).where(customer_counts.c.transaction_count > 1)

        total_customers = conn.execute(total_customers_stmt).scalar() or 0
        repeat_customers = conn.execute(repeat_customers_stmt).scalar() or 0

    retention_rate = 0.0
    if total_customers:
        retention_rate = round((repeat_customers / total_customers) * 100, 2)

    return {
        "total_customers": int(total_customers),
        "repeat_customers": int(repeat_customers),
        "customer_retention_rate": retention_rate,
    }


def get_transaction_summary():
    with engine.connect() as conn:
        stmt = select(
            func.count().label("total_transactions"),
            func.sum(transactions.c.amount).label("total_volume"),
        )
        row = conn.execute(stmt).one()
    return {
        "total_transactions": int(row.total_transactions or 0),
        "total_volume": float(row.total_volume or 0),
    }


def get_customer_segments():
    with engine.connect() as conn:
        customer_segment = (
            select(
                transactions.c.customer_id,
                func.avg(transactions.c.amount).label("avg_amount"),
            )
            .group_by(transactions.c.customer_id)
            .subquery()
        )

        stmt = select(
            func.sum(case((customer_segment.c.avg_amount >= 200, 1), else_=0)).label("high_value_customers"),
            func.sum(case((customer_segment.c.avg_amount.between(100, 199.99), 1), else_=0)).label("mid_value_customers"),
            func.sum(case((customer_segment.c.avg_amount < 100, 1), else_=0)).label("low_value_customers"),
        )
        result = conn.execute(stmt).one()

    return {
        "high_value_customers": int(result.high_value_customers or 0),
        "mid_value_customers": int(result.mid_value_customers or 0),
        "low_value_customers": int(result.low_value_customers or 0),
    }
