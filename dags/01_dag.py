from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id='primer_dag',
    start_date=datetime(2025, 12, 18),
    # schedule_interval='@once',
    catchup=False
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')
    start >> end
