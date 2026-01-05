from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.sensors.filesystem import FileSensor

with DAG(dag_id="7_3_filesensor",
         description="FileSensor",
         schedule="* * * * *",
         start_date=datetime(2026, 1, 4),
         # end_date=datetime(2026, 1, 4),
         # max_active_runs=1
         ) as dag:

    t1 = BashOperator(task_id="creating_file",
                      bash_command="sleep 10 && touch /tmp/file.txt")

    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/file.txt")

    t3 = BashOperator(task_id="end_task",
                      bash_command="echo 'El fichero ha llegado'")

    t1 >> t2 >> t3
