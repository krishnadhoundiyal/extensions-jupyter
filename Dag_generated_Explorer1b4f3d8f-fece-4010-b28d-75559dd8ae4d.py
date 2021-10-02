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
    "Dag_generated_Explorer1b4f3d8f-fece-4010-b28d-75559dd8ae4d",
    default_args=default_args,
    description="Take This from User",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["example"],
)

op_d25762dd7b244f14af6bb2a0031bb863 = NotebookOperator(
    task_id="d25762dd7b244f14af6bb2a0031bb863",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_32fa75f886b34a48a72fddc4c9e237fe = NotebookOperator(
    task_id="32fa75f886b34a48a72fddc4c9e237fe",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_8c20677046ae47408053f2cd5bedcc0f = NotebookOperator(
    task_id="8c20677046ae47408053f2cd5bedcc0f",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_d25762dd7b244f14af6bb2a0031bb863 >> op_32fa75f886b34a48a72fddc4c9e237fe

op_32fa75f886b34a48a72fddc4c9e237fe >> op_8c20677046ae47408053f2cd5bedcc0f
