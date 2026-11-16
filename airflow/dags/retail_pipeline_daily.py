from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="retail_pipeline_daily",
    start_date=datetime(2025, 1, 1),
    schedule="@hourly",
    catchup=False,
) as dag:

    BashOperator(
        task_id="run_pipeline",
        bash_command="cd /opt/airflow/pipeline && python src/main.py",
    )