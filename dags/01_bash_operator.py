from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='bash_operator',
    tags=['bash operator'],
    start_date=datetime(2025, 12, 18),
) as dag:

    # [START howto_operator_bash]
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )
    # [END howto_operator_bash]

    # [START howto_operator_bash_template]
    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )
    # [END howto_operator_bash_template]

    t3 = BashOperator(
        task_id='templated',
        bash_command="""
        {% for i in range(5) %}
            echo "{{ ds }}"
            echo "{{ macros.ds_add(ds, 7) }}"
            echo "{{ params.my_param }}"
        {% endfor %}
        """,
        params={'my_param': 'Parameter I passed in'},
    )

    t1 >> [t2, t3]
