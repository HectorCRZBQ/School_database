from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from insert import insert_all

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

dag = DAG(
    'dag2',
    default_args=default_args,
    description='Insert data',
    schedule_interval=None,
)

t = PythonOperator(
    task_id='t',
    python_callable=insert_all,
    dag=dag
)