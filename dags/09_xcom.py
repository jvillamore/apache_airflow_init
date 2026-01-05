from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

with DAG(dag_id="09_xcom",
         description="XCom Example",
         schedule="* * * * *",
         start_date=datetime(2026, 1, 4),
         # end_date=datetime(2026, 1, 4),
         # max_active_runs=1
         ) as dag:

    t1 = BashOperator(task_id="multiply_numbers",
                      bash_command="sleep 5 && echo $((3 * 9))")

    t2 = BashOperator(task_id="obtain_result",
                      bash_command="sleep 5 && RESULT={{ ti.xcom_pull(task_ids='multiply_numbers') }} && echo El resultado es $RESULT")

    t3 = PythonOperator(task_id="print_result",
                        python_callable=lambda ti: print(f"El resultado obtenido es {ti.xcom_pull(task_ids='obtain_result')}"))

    t1 >> t2 >> t3
