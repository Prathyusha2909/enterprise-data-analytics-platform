# Enterprise Data Analytics Platform

An end-to-end analytics platform for processing, analyzing, and exposing large-scale business transaction datasets.

## Tech Stack

- Python
- SQL
- PostgreSQL
- Pandas
- FastAPI
- Power BI (dashboarding)

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

## GitHub Project Entry

This project can be published to GitHub as a complete analytics platform repository. Add the repository to GitHub, then push your local branch:

```powershell
git init
git add .
git commit -m "Initial analytics platform scaffold"
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Extensions

- Add Power BI dataset definitions and `.pbix` files in a `powerbi/` folder
- Add additional pipeline sources under `data/raw/`
- Build incremental load and scheduling with Airflow, Prefect, or cron
