import logging
import airflow
import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from datetime import timedelta

from airflow.operators.python_operator import PythonOperator

dag = DAG(
  dag_id = "bigquery_execute",
  start_date = airflow.utils.dates.days_ago(1),
  schedule_interval = "0 0 * * *",
  catchup = True
)

# example result: 2018-10-27
today = datetime.datetime.now().strftime('%Y-%m-%d')

yesterday = today - timedelta(1)
yesterday_string = yesterday.strftime('%Y-%m-%d')

bigquery_execute = BashOperator(
  task_id = "bigquery_execute",
  # resulting command: cd work && python main.py 2018-10-26 2018-10-27
  # the two parameter start date and end date will be passed on into the SQL query
  bash_command = "cd /work && python main.py " + yesterday_string + " " + today,
  dag = dag
)

bigquery_execute
