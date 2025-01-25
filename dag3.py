from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from create_audit_tables import create_tables

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

dag = DAG(
    'dag3',
    default_args=default_args,
    description='Insert data',
    schedule_interval=None,
)

t = PythonOperator(
    task_id='t',
    python_callable=create_tables,
    dag=dag
)