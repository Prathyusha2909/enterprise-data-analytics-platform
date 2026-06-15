# Enterprise Data Analytics Platform

An end-to-end analytics platform for processing, analyzing, and exposing large-scale business transaction datasets.

## Tech Stack

- Python
- SQL
- PostgreSQL
- Pandas
- FastAPI
- Power BI (dashboarding)

## Project Summary

Enterprise Data Analytics Platform | GitHub

Tech Stack: Python, SQL, PostgreSQL, Pandas, Power BI, FastAPI

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
- REST API endpoints powered by FastAPI to expose analytics and KPI results
- Reporting-ready architecture for Power BI dashboards and internal integrations

## Key Features

- Automated data ingestion and transformation
- PostgreSQL-backed curated analytics tables
- KPI summary endpoints for revenue, transaction volume, and retention
- Modular pipeline for easy extension to new business domains

## Architecture Flow

Raw Data → Python ETL → PostgreSQL Analytics Tables → FastAPI KPI APIs → Power BI Dashboard

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

## Extensions

- Add Power BI dataset definitions and `.pbix` files in the `powerbi/` folder
- Add additional pipeline sources under `data/raw/`
- Build incremental load and scheduling with Airflow, Prefect, or cron
