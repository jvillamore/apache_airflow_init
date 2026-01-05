from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import BranchPythonOperator
from airflow.sdk import TriggerRule


def _choose_branch(**kwargs):
    fecha = kwargs["logical_date"]
    print(f"La fecha es {fecha}")
    # Example of using kwargs if needed
    if fecha.second % 2 == 0:
        return 'even_task'
    else:
        return 'odd_task'


with DAG(dag_id="10_branch_python_operator",
         description="Branch Python Operator Example",
         schedule="* * * * *",
         start_date=datetime(2026, 1, 4),
         # end_date=datetime(2026, 1, 4),
         # max_active_runs=1
         ) as dag:
    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=_choose_branch
    )

    even_task = BashOperator(
        task_id='even_task',
        bash_command='echo "This is the even task"'
    )

    odd_task = BashOperator(
        task_id='odd_task',
        bash_command='echo "This is the odd task"'
    )
    final_task = BashOperator(
        task_id='final_task',
        bash_command='echo "This is the final task"',
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS
    )

    branching >> [even_task, odd_task]
    [even_task, odd_task] >> final_task
