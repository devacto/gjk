## Question 1
Query can be found [here](https://github.com/devacto/gjk/blob/qn-one/query.sql).

Screenshot below shows the result when the query is being submitted to BigQuery.

![bigquery_result](https://raw.githubusercontent.com/devacto/gjk/master/docs/images/big_query_screenshot.png)

## Question 2
An example Airflow pipeline definition can be found [here]().

Backfilling can be done using `catchup = True` parameter in the DAG definition.

Screenshot below shows how start date (yesterday) and end date (today) are
passed in as parameters.

<img src="https://raw.githubusercontent.com/devacto/gjk/master/docs/images/bigquery_bash_operator.png" width="500" />

## Question 3
The Python script can be found [here](https://github.com/devacto/gjk/blob/qn-three/main.py).

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

## Question 5
The diagram below shows the architecture I would be aiming for, given the opportunity.

![proposed_architecture](https://raw.githubusercontent.com/devacto/gjk/master/docs/images/proposed_architecture.png)

The major change will be to use Kafka Streams and KSQL to do real-time processing of data that goes into BigQuery data warehouse.

This way, data in BigQuery data warehouse can be made near-real-time instead of several hours late because of batch processing.

Batch processing infrastructure is still present for data exploration purpose.

Data redaction can also be done in real-time using KSQL.

## Question 6
Answers for Question 6 can be found [here](https://docs.google.com/document/d/12pVDFa10Ho8AC-NdooQ3umCjK0mQ6QMsjq-DKSFj33M/edit?usp=sharing).