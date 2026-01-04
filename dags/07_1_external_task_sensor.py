from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id='7_1_external_task_sensor',
    tags=['bash operator'],
    schedule='* * * * *',
    start_date=datetime(2026, 1, 4),
) as dag:
    t1 = BashOperator(
        task_id='print_date',
        bash_command='sleep 10 && echo date',
        depends_on_past=True
    )
    t1
