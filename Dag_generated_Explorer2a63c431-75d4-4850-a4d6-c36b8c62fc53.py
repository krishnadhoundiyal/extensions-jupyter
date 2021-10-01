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
    "Dag_generated_Explorer2a63c431-75d4-4850-a4d6-c36b8c62fc53",
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

op_41f69e14cf4449ee90694e00fe7e5cbd = NotebookOperator(
    task_id="41f69e14cf4449ee90694e00fe7e5cbd",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_16528496c8dc4ceab2cfc2c9acd11a0f = NotebookOperator(
    task_id="16528496c8dc4ceab2cfc2c9acd11a0f",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_0aa52912f8c34320830e808e0a6a4e25 = NotebookOperator(
    task_id="0aa52912f8c34320830e808e0a6a4e25",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_003bbdffbd4d490da994d796243f28a7 >> op_468f7ed8ed774f3e9e920780227cd33a

op_003bbdffbd4d490da994d796243f28a7 >> op_41f69e14cf4449ee90694e00fe7e5cbd

op_468f7ed8ed774f3e9e920780227cd33a >> op_16528496c8dc4ceab2cfc2c9acd11a0f

op_41f69e14cf4449ee90694e00fe7e5cbd >> op_16528496c8dc4ceab2cfc2c9acd11a0f

op_16528496c8dc4ceab2cfc2c9acd11a0f >> op_0aa52912f8c34320830e808e0a6a4e25
