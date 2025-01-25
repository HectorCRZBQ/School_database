from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from create_databases import create_databases
from create_main_tables import create_tables

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

dag = DAG(
    'dag1',
    default_args=default_args,
    description='Create database and create tables',
    schedule_interval=None,
)

t1 = PythonOperator(
    task_id='t1',
    python_callable=create_databases,
    dag=dag
)

t2 = PythonOperator(
    task_id='t2',
    python_callable=create_tables,
    dag=dag
)

t1 >> t2