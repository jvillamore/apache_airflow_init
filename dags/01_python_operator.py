from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def my_python_function():
    print("Hello from my Python function!")


with DAG(
    dag_id='first_python_operator',
    start_date=datetime(2025, 12, 18),
    description='A simple DAG with a PythonOperator',
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='run_python_function',
        python_callable=my_python_function,
    )

    t1
