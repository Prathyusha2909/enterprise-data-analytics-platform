# Enterprise Data Analytics Platform: ETL, Analytics & KPI Reporting System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)

An end-to-end analytics platform for processing, analyzing, and exposing large-scale business transaction datasets.

## Business Problem

Organizations often struggle with fragmented transactional data, delayed reporting, and limited visibility into operational KPIs. This platform centralizes data ingestion, analytics, reporting, and KPI exposure through a unified analytics architecture.

## Business Value

The platform enables organizations to transform fragmented transactional data into actionable business insights through automated ETL workflows, centralized analytics storage, KPI monitoring, and self-service reporting.

## Tech Stack

- Python
- SQL
- PostgreSQL
- Pandas
- FastAPI
- Power BI

## Highlights
- Built an end-to-end enterprise analytics platform for processing and analyzing large-scale business transaction datasets using Python, SQL, and PostgreSQL.
- Designed ETL pipelines for data ingestion, cleansing, validation, transformation, and loading curated datasets into PostgreSQL for downstream analytics and reporting.
- Performed exploratory data analysis (EDA) and KPI discovery to identify trends in customer behavior, revenue performance, transaction volume, and operational efficiency.
- Developed interactive Power BI dashboards for visualizing business metrics, customer insights, and operational KPIs to support data-driven decision-making.
- Automated reporting workflows using Python and SQL, improving data accessibility and reducing manual reporting effort.
- Built FastAPI-based REST services to expose analytics insights and KPI summaries for integration with internal applications and reporting systems.

## Project Overview

This repository demonstrates a scalable analytics workflow including:

- ETL pipeline to ingest raw transaction data from heterogeneous sources
- Data cleansing, validation, and transformation using Pandas
- Curated dataset storage in PostgreSQL
- REST API endpoints powered by FastAPI to expose analytics insights, KPI summaries, and reporting data
- Reporting-ready architecture for Power BI dashboards and internal integrations

## Key Features

- Automated data ingestion and transformation
- PostgreSQL-backed curated analytics tables
- KPI summary endpoints for revenue, transaction volume, and retention
- Modular pipeline for easy extension to new business domains

## Dataset

The platform is designed to process transaction datasets containing:

- Customer records
- Sales transactions
- Product information
- Revenue and retention metrics

The architecture supports scalable processing through modular ETL pipelines and analytics-ready storage layers.

## System Architecture

![Architecture](docs/architecture.png)

## Dashboard Preview

![Power BI Dashboard](powerbi/dashboard.png)

## Repository Structure

enterprise-data-analytics-platform/
├── app/
│   ├── analytics.py
│   ├── etl.py
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   └── models.py
├── sql/
│   └── schema.sql
├── data/
│   ├── raw/
│   │   └── sample_transactions.csv
│   └── sample_transactions.csv
├── powerbi/
│   ├── dashboard.pbix
│   ├── dashboard.png
│   └── README.md
├── docs/
│   ├── architecture.md
│   ├── data-model.md
│   ├── deployment.md
│   ├── visualization.md
│   └── README.md
├── requirements.txt
└── README.md

## Sample KPIs

The platform exposes analytics for:

- Total Revenue
- Monthly Revenue Growth
- Customer Retention Rate
- Transaction Volume
- Average Order Value
- Customer Segmentation Metrics

## Example API Endpoints

GET /kpis/revenue
GET /kpis/retention
GET /kpis/transactions
GET /analytics/customer-segments

### Sample API Responses

**GET /kpis/revenue**
```json
{
  "total_revenue": 824450.75,
  "monthly_revenue_growth": 12.5
}
```

**GET /kpis/retention**
```json
{
  "total_customers": 1200,
  "repeat_customers": 340,
  "customer_retention_rate": 28.3
}
```

**GET /kpis/transactions**
```json
{
  "total_transactions": 15840,
  "total_volume": 824450.75
}
```

**GET /analytics/customer-segments**
```json
{
  "high_value_customers": 280,
  "mid_value_customers": 600,
  "low_value_customers": 320
}
```

## Deployment

The platform can be deployed using:

- Azure App Service + Azure Database for PostgreSQL
- AWS EC2 + RDS PostgreSQL
- GCP Compute Engine + Cloud SQL

## Setup

1. Create a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy environment variables:

```powershell
copy .env.example .env
```

4. Update `.env` with your PostgreSQL connection string.

5. Create the analytics schema in PostgreSQL:

```powershell
psql %DATABASE_URL% -f sql\schema.sql
```

## Usage

Run the ETL pipeline:

```powershell
python -m app.etl
```

Start the FastAPI server:

```powershell
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` to explore the API.

## Documentation

For deeper architecture, modeling, and deployment details, see the `docs/` folder:

- `docs/architecture.md` — system architecture and data flow
- `docs/data-model.md` — data modeling and analytical schema design
- `docs/deployment.md` — Azure/AWS cloud deployment guidance
- `docs/visualization.md` — report and Power BI dashboard guidance
