from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from search_elasticsearch import elasticsearch_main

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
    python_callable=elasticsearch_main('https://www.ucjc.edu'),
    dag=dag
)