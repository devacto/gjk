import logging
import airflow

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

from airflow.operators.python_operator import PythonOperator

dag = DAG(
  dag_id = "convert_csv_to_json",
  start_date = airflow.utils.dates.days_ago(1),
  schedule_interval = None
)

convert_csv_to_json = BashOperator(
  task_id = "convert_csv_to_json",
  bash_command = "python main.py",
  dag = dag
)

convert_csv_to_json