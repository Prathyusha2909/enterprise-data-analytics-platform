# Architecture

This document describes the overall Enterprise Data Analytics Platform architecture.

## System Components

- **Data Ingestion**: Raw CSV and source data files are ingested into the platform and validated.
- **ETL Pipeline**: Python-based ETL scripts perform cleansing, validation, enrichment, and transformation of raw inputs.
- **Data Warehouse**: PostgreSQL stores curated tables and supports analytics queries.
- **Analytics API**: FastAPI exposes KPI summaries and transaction metrics for downstream applications.
- **BI Visualization**: Power BI dashboards connect to PostgreSQL to visualize revenue, customer retention, transaction volume, and operational metrics.

## Data Flow

1. Raw data files are placed into `data/raw/`.
2. The ETL pipeline loads and validates data using `app/etl.py`.
3. Cleaned data is stored in PostgreSQL via `sql/schema.sql` and SQLAlchemy models.
4. FastAPI serves analytics and KPI endpoints from the curated database.
5. Power BI visuals and dashboards consume analytics results and published datasets.

## Architecture Notes

- The design is modular so source connectors, transformation logic, and destination schemas can be extended independently.
- A cloud deployment can host PostgreSQL on managed services, run ETL in containers or serverless functions, and publish BI dashboards through Power BI Service or AWS QuickSight.
