from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

from scripts.load_bronze import load_bronze

with DAG(
    dag_id="medallion_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    bronze = PythonOperator(
        task_id="load_bronze",
        python_callable=load_bronze
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt && dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/dbt && dbt test"
    )

    bronze >> dbt_run >> dbt_test