from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def my_python_function():
    print("Hello from my Python function!")


def python_task():
    print("This is a Python task 3.")


with DAG(
    dag_id='03_dependencias_entre_tareas',
    start_date=datetime(2025, 12, 18),
    description='Creando dependencias entre tareas',
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='run_python_function',
        python_callable=my_python_function,
    )

    t2 = BashOperator(
        task_id='task_number_two',
        bash_command='echo "Example of task dependencies in Airflow!"',
    )

    t3 = PythonOperator(
        task_id='run_python_function_task_3',
        python_callable=python_task,
    )

    t4 = BashOperator(
        task_id='task_number_four',
        bash_command='echo "Example of task dependencies in Airflow! Task 4."',
    )

    # Definición con set_downstream
    # t1.set_downstream(t2)
    # t2.set_downstream([t3, t4])

    # Definición con operador >>
    t1 >> t2 >> [t3, t4]
