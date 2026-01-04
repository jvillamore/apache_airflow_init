from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.sensors.external_task import ExternalTaskSensor

with DAG(
    dag_id='7_2_external_task_sensor',
    description='DAG que utiliza ExternalTaskSensor para depender de otra DAG',
    tags=['bash operator'],
    schedule='* * * * *',
    start_date=datetime(2026, 1, 4),
) as dag:
    t1 = ExternalTaskSensor(
        task_id='7_2_wait_for_7_1_external_task_sensor',
        external_dag_id='7_1_external_task_sensor',
        external_task_id='print_date',
        poke_interval=10,  # segundos entre cada intento
        timeout=600,     # tiempo máximo de espera en segundos
        mode='poke',      # modo de operación del sensor
        depends_on_past=True
    )

    t2 = BashOperator(
        task_id='echo_final',
        bash_command='echo "Tarea finalizada"',
    )
    t1 >> t2
