from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="simulator_hourly",
    schedule="@hourly",
    catchup=False,
    start_date=datetime(2025, 1, 1),
):

    BashOperator(
        task_id="generate_data",
        bash_command="cd /opt/airflow/simulator && python src/run_daily.py",
    )