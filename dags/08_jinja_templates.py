from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


templated_command = """
{% for file in params.filenames %}
    echo "{{ ds }}"
	echo "{{ file }}"
{% endfor %}
"""


with DAG(dag_id="08-templating",
         description="Example using templates",
         schedule="* * * * *",
         start_date=datetime(2025, 1, 4),
         # max_active_runs=1
         ) as dag:

    t1 = BashOperator(task_id="tarea_1",
                      bash_command=templated_command,
                      params={"filenames": ["file1.txt", "file2.txt"]},
                      depends_on_past=True)

    t1
