from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="05_1_orquestacion",
    description="Orquestación de tareas con dependencias simples",
    schedule='* * * * *',
    start_date=datetime(2025, 12, 29),
    end_date=datetime(2025, 12, 30),
    default_args={
        'depends_on_past': True,
        'max_active_runs': 1,
    }
) as dag:
    t1 = BashOperator(
        task_id='tarea_1',
        bash_command='echo "Ejecutando tarea 1"'
    )
    t2 = BashOperator(
        task_id='tarea_2',
        bash_command='sleep 2 && echo "Ejecutando tarea 2"'
    )
    t3 = BashOperator(
        task_id='tarea_3',
        bash_command='sleep 2 && echo "Ejecutando tarea 3"'
    )
    t4 = BashOperator(
        task_id='tarea_4',
        bash_command='sleep 2 &&echo "Ejecutando tarea 4"'
    )

    t1 >> t2 >> [t3, t4]
