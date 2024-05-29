from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator, DatabricksRunNowOperator
from datetime import datetime, timedelta 

########## NB: Replace <your_UserId> with your own details ##########

#Define params for Submit Run Operator
notebook_task = {
    'notebook_path': '/Workspace/Users/umarchemi5t@gmail.com/_2_batch_data_processing_from_mounted_s3',
}


#Define params for Run Now Operator
notebook_params = {
    "Variable":5
}


default_args = {
    'owner': 'UmarB',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


with DAG('<your_UserId>_dag',
    # should be a datetime format
    start_date=datetime(2024, 4, 24),
    # check out possible intervals, should be a string
    schedule_interval='@daily',
    catchup=False,
    default_args=default_args
    ) as dag:


    opr_submit_run = DatabricksSubmitRunOperator(
        task_id='submit_run',
        # the connection we set-up previously
        databricks_conn_id='databricks_default',
        existing_cluster_id='1108-162752-8okw8dgg',
        notebook_task=notebook_task
    )
    opr_submit_run
