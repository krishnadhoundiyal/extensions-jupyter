from airflow.operators.notebook import NotebookOperator
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
import datetime

default_args = {
    "owner": "airflow_user1",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}
dag = DAG(
    "Dag_generated_Explorer1d2848a4-b612-4dc6-9caf-a9ac8fa35ad7",
    default_args=default_args,
    description="Take This from User",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["example"],
)

op_003bbdffbd4d490da994d796243f28a7 = NotebookOperator(
    task_id="003bbdffbd4d490da994d796243f28a7",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_468f7ed8ed774f3e9e920780227cd33a = NotebookOperator(
    task_id="468f7ed8ed774f3e9e920780227cd33a",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_003bbdffbd4d490da994d796243f28a7 >> op_468f7ed8ed774f3e9e920780227cd33a
