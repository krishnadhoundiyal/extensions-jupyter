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
    "Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb",
    default_args=default_args,
    description="Take This from User",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=["example"],
)

op_3b7cf0d315bf45ea820ed29ee4687ca7 = NotebookOperator(
    task_id="3b7cf0d315bf45ea820ed29ee4687ca7",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_4b33b55c85004a1dbad5c3b15e4a0702 = NotebookOperator(
    task_id="4b33b55c85004a1dbad5c3b15e4a0702",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_29b1d1bae54d48b5b0b3e66cded365ac = NotebookOperator(
    task_id="29b1d1bae54d48b5b0b3e66cded365ac",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_4b4f06f328ff4a788473eb9281948b81 = NotebookOperator(
    task_id="4b4f06f328ff4a788473eb9281948b81",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_3be3433fa22242d1a3fbeeeb7158b571 = NotebookOperator(
    task_id="3be3433fa22242d1a3fbeeeb7158b571",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_9bf5f55dc5b64bc2bf4687def5d421ef = NotebookOperator(
    task_id="9bf5f55dc5b64bc2bf4687def5d421ef",
    NoteBookCommands="Will add them here later",
    dag=dag,
)

op_3b7cf0d315bf45ea820ed29ee4687ca7 >> op_4b33b55c85004a1dbad5c3b15e4a0702

op_3b7cf0d315bf45ea820ed29ee4687ca7 >> op_9bf5f55dc5b64bc2bf4687def5d421ef

op_4b33b55c85004a1dbad5c3b15e4a0702 >> op_29b1d1bae54d48b5b0b3e66cded365ac

op_29b1d1bae54d48b5b0b3e66cded365ac >> op_4b4f06f328ff4a788473eb9281948b81

op_29b1d1bae54d48b5b0b3e66cded365ac >> op_3be3433fa22242d1a3fbeeeb7158b571
