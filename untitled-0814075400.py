from airflow.operators.bash_operator import BashOperator
from airflow import DAG

from airflow.kubernetes.secret import Secret

from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled-0814075400",
}

dag = DAG(
    "untitled-0814075400",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 3.1.0.dev0 pipeline editor using `untitled.pipeline`.",
    is_paused_upon_creation=False,
)


# Ensure that the secret named '0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
    key="AWS_SECRET_ACCESS_KEY",
)


op_1a22aff7_703e_4034_9a49_8f25802689cc = BashOperator(
    namespace="default",
    task_id="BashOperator",
    bash_command='echo "Hellow"',
    xcom_push=False,
    env={},
    output_encoding="utf-8",
    inputs=[],
    outputs=[],
    secrets=[env_var_secret_id, env_var_secret_key],
    in_cluster=True,
    config_file="None",
    dag=dag,
)
