from airflow.operators.bash_operator import BashOperator
from airflow import DAG

from airflow.kubernetes.secret import Secret

from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled-0814082113",
}

dag = DAG(
    "untitled-0814082113",
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


op_5e068f70_f6f8_4d9c_881c_522210c39271 = KubernetesPodOperator(
    name="untitled",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/master/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint https://storage.googleapis.com --cos-bucket airflowelyrabucket --cos-directory 'untitled-0814082113' --cos-dependencies-archive 'untitled-5e068f70-f6f8-4d9c-881c-522210c39271.tar.gz' --file 'work/untitled.py' "
    ],
    task_id="untitled",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled-0814082113-{{ ts_nodash }}",
    },
    secrets=[env_var_secret_id, env_var_secret_key],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_5e068f70_f6f8_4d9c_881c_522210c39271 << op_1a22aff7_703e_4034_9a49_8f25802689cc
