from airflow import DAG
from operators.hello_operator import HelloOperator
import datetime


with DAG(
    dag_id='04_custom_operator',
    start_date=datetime.datetime(2025, 12, 18),
    description='Utilizando un operador personalizado',
    catchup=False
) as dag:
    custom_task = HelloOperator(
        task_id='Hello_Custom_Operator_Task',
        name='Custom_Operator'
        # my_param='Ricarda'
    )
    custom_task
