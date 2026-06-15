# Data Modeling

This project uses a simple analytic model optimized for transaction-level reporting.

## Core Entity: transactions

| Column | Type | Description |
|---|---|---|
| transaction_id | TEXT | Unique transaction identifier |
| transaction_date | TIMESTAMP | Transaction timestamp |
| customer_id | TEXT | Customer identifier |
| amount | NUMERIC(12,2) | Transaction revenue amount |
| product_category | TEXT | Product or service category |
| business_unit | TEXT | Business unit or line of business |
| status | TEXT | Transaction status |

## Analytical Design

- The `transactions` table is a fact table used for KPI and trend analysis.
- Additional dimension tables can be added for customers, products, and time to support a star schema.
- Current design supports aggregated metrics, customer counts, and trend analysis over time.
