from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime


def my_python_task():
    print("Ejecutando tarea 4")
    # raise Exception("Fallo intencional de la tarea 4 para monitoreo")


with DAG(
    dag_id="06_monitoring",
    description="Orquestación de tareas con cronjob",
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
    t4 = PythonOperator(
        task_id='tarea_4',
        python_callable=my_python_task
    )

    t1 >> t2 >> [t3, t4]
