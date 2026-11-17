# Cloud Data Platform

A production-style cloud ETL pipeline built with **Python, Apache Airflow, Docker, PostgreSQL, and Google BigQuery**.

This project simulates a real-world retail data platform by generating transactional data, performing incremental ETL, loading data into BigQuery, and building analytical tables for reporting.

## Live Dashboard

**[View the Retail Sales Performance dashboard →](https://datastudio.google.com/u/0/reporting/e83a2e39-a80e-498e-9cc5-79787f35f66c/page/kUhDG)**

![Dashboard preview](docs/dashboard.png)

Built in Looker Studio on top of the BigQuery analytics tables. Data is refreshed hourly by the Airflow pipeline.
---

## Architecture

```
                 +----------------------+
                 |   Data Simulator     |
                 |  (Python Scheduler)  |
                 +----------+-----------+
                            |
                            |
                            ▼
                  Cloud SQL / PostgreSQL
                            |
                            |
                     Incremental Extract
                            |
                            ▼
                    Data Validation
                            |
                            ▼
                    Data Transformation
                            |
                            ▼
                     Google BigQuery
                            |
            +---------------+----------------+
            |               |                |
            ▼               ▼                ▼
      Sales Summary   Daily Sales     Top Products
                            |
                            ▼
                    Looker Studio
```

---

# Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3 |
| Workflow | Apache Airflow |
| Container | Docker |
| Database | PostgreSQL |
| Cloud Warehouse | Google BigQuery |
| ORM | SQLAlchemy |
| Analytics | BigQuery SQL |
| Dashboard | Looker Studio |

---

# Features

## Incremental ETL Pipeline

The pipeline only extracts records created after the last successful execution.

```
Metadata Table
        │
        ▼
last_run
        │
        ▼
Extract New Rows
        │
        ▼
Validate
        │
        ▼
Transform
        │
        ▼
Load BigQuery
        │
        ▼
Update Metadata
```

---

## Data Validation

Before loading into BigQuery, every record passes validation.

Examples include:

- Required field validation
- Duplicate detection
- Invalid value rejection
- Data type verification

Rejected rows are excluded from loading and recorded in the pipeline log.

---

## Metadata Management

A metadata table stores pipeline execution status.

Example fields:

| Column | Description |
|---------|-------------|
| pipeline_name | ETL pipeline name |
| last_run | Last successful execution |
| status | SUCCESS / FAILED |
| rows_loaded | Number of rows loaded |

This enables:

- Incremental loading
- Safe reruns
- Idempotent execution

---

## Logging

Each ETL stage produces detailed logs including:

- Extracted rows
- Validated rows
- Rejected rows
- Loaded rows
- Execution duration
- Pipeline status

Example:

```
========== customers ==========

Status      : SUCCESS
Extracted   : 153
Validated   : 152
Rejected    : 1
Loaded      : 152
Duration    : 0.98 sec
```

---

## Alerting

The pipeline sends email alerts through Gmail SMTP in two cases:

| Alert | Trigger |
|---|---|
| Pipeline failure | Any stage raises an exception; the email includes the pipeline name and the error |
| High reject rate | More than 5% of extracted rows fail validation |

The second case matters most: the run still succeeds and Airflow shows green, so without this alert a source data problem would go unnoticed. Rejected rows are kept in the `rejected_rows` table in BigQuery for investigation.

Alerting is optional. If the email settings are not configured, the pipeline logs a warning and continues.


## Airflow Scheduling

Apache Airflow orchestrates the pipeline.

Current DAG:

```
retail_pipeline
        │
        ▼
 run_pipeline
```

The pipeline executes automatically every hour.

```
@hourly
```

---

# Project Structure

```
cloud-data-platform/

│
├── airflow/
│   ├── dags/
│   ├── docker-compose.yml
│   └── Dockerfile
│
├── pipeline/
│   ├── src/
│   │
│   ├── analytics/
│   ├── common/
│   ├── extract/
│   ├── load/
│   ├── metadata/
│   ├── models/
│   ├── pipeline/
│   ├── transform/
│   ├── validate/
│   └── main.py
│
├── simulator/
│
├── credentials/
│
└── README.md
```

---

# Analytics Tables

The pipeline automatically generates analytical tables.

- Sales Summary
- Daily Sales
- Top Products
- Top Customers
- Category Sales

These tables are rebuilt after every ETL execution.

---

# Pipeline Flow

```
PostgreSQL
      │
      ▼
Extract
      │
      ▼
Validate
      │
      ▼
Transform
      │
      ▼
Load BigQuery
      │
      ▼
Update Metadata
      │
      ▼
Generate Analytics Tables
```

---

# Running the Project

## Start Airflow

```bash
docker compose up
```

Open:

```
http://localhost:8080
```

---

## Run Pipeline Manually

```bash
python src/main.py
```

---

## Airflow Execution

The pipeline runs automatically every hour.

Airflow executes:

```bash
cd /opt/airflow/pipeline && python src/main.py
```

---

# Future Improvements

- Separate Airflow tasks (Extract → Validate → Transform → Load)
- dbt integration
- Unit testing
- CI/CD with GitHub Actions
- Cloud Run deployment
- Data quality monitoring
- Slack/Email notifications

---

# Skills Demonstrated

- Data Engineering
- ETL Pipeline Design
- Apache Airflow
- Incremental Data Loading
- SQLAlchemy
- Docker
- PostgreSQL
- Google BigQuery
- Logging & Monitoring
- Metadata Management
- Analytics Engineering