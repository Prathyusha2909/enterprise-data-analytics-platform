from sqlalchemy import Table, Column, Text, Numeric, TIMESTAMP, MetaData
from .db import metadata

transactions = Table(
    "transactions",
    metadata,
    Column("transaction_id", Text, primary_key=True),
    Column("transaction_date", TIMESTAMP, nullable=False),
    Column("customer_id", Text, nullable=False),
    Column("amount", Numeric(12, 2), nullable=False),
    Column("product_category", Text),
    Column("business_unit", Text),
    Column("status", Text),
)
