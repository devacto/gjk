## Question 1
Query can be found [here](https://github.com/devacto/gjk/blob/qn-one/query.sql).

Screenshot below shows the result when the query is being submitted to BigQuery.

![bigquery_result](https://raw.githubusercontent.com/devacto/gjk/master/docs/images/big_query_screenshot.png)

## Question 2
Test question 2.

## Question 3
Test Question 3.

## Question 4
The Docker Compose file can be found [here](https://github.com/devacto/gjk/blob/qn-four/docker-compose.yml).

Screenshot from Apache Airflow that shows CSV conversion scheduled to be run on
a daily basis, and its status.

![airflow_dag_details](https://raw.githubusercontent.com/devacto/gjk/master/docs/images/airflow_dag_details.png)

To start the Docker containers that starts up Airflow, use the command below:

```
docker-compose -f qn-four/docker-compose.yml up
```

To stop and remove the Docker containers, use the command below:

```
docker-compose -f qn-four/docker-compose.yml down
```