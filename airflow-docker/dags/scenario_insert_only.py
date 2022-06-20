import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

dag = DAG(
    dag_id='scenario_insert_only',
    default_args={
        'owner': 'Airflow',
        'start_date': airflow.utils.dates.days_ago(0),
    }
)

run_this = BashOperator(
    task_id='run_this',
    bash_command='python /opt/airflow/dags/script/transfer_case_insert_only.py',
    dag=dag,
)

run_this 

