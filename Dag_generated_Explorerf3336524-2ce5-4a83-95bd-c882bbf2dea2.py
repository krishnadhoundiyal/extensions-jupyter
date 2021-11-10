from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorerf3336524-2ce5-4a83-95bd-c882bbf2dea2",
}

dag = DAG(
    "Dag_generated_Explorerf3336524-2ce5-4a83-95bd-c882bbf2dea2",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Take This from User",
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


op_99a6378a5922434f806e65e9fb03d38e = KubernetesPodOperator(
    task_id="99a6378a5922434f806e65e9fb03d38e",
    name="99a6378a5922434f806e65e9fb03d38e",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorerf44e0471-a1b5-464c-9ad3-582d1b27cfb4' --dependencies-archive 'load_data-99a6378a5922434f806e65e9fb03d38e.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorerf44e0471-a1b5-464c-9ad3-582d1b27cfb4",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_07bcf3c366084b0083dff345c3c8c6cf = KubernetesPodOperator(
    task_id="07bcf3c366084b0083dff345c3c8c6cf",
    name="07bcf3c366084b0083dff345c3c8c6cf",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorerf44e0471-a1b5-464c-9ad3-582d1b27cfb4' --dependencies-archive 'Part 1 - Data Cleaning-07bcf3c366084b0083dff345c3c8c6cf.tar.gz' --file '/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "g": "h",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorerf44e0471-a1b5-464c-9ad3-582d1b27cfb4",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_ac6d656939964b96928ce14fd10d49a5 = KubernetesPodOperator(
    task_id="ac6d656939964b96928ce14fd10d49a5",
    name="ac6d656939964b96928ce14fd10d49a5",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorerf44e0471-a1b5-464c-9ad3-582d1b27cfb4' --dependencies-archive 'Part 3 - Time Series Forecasting-ac6d656939964b96928ce14fd10d49a5.tar.gz' --file '/Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/forecasted.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "f",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorerf44e0471-a1b5-464c-9ad3-582d1b27cfb4",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_e0061ec3ab2c4cac9d7ca29b5f4b692a = KubernetesPodOperator(
    task_id="e0061ec3ab2c4cac9d7ca29b5f4b692a",
    name="e0061ec3ab2c4cac9d7ca29b5f4b692a",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorerf44e0471-a1b5-464c-9ad3-582d1b27cfb4' --dependencies-archive 'Part 2 - Data Analysis-e0061ec3ab2c4cac9d7ca29b5f4b692a.tar.gz' --file '/Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/datanalysis.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "ff",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorerf44e0471-a1b5-464c-9ad3-582d1b27cfb4",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_99a6378a5922434f806e65e9fb03d38e >> op_07bcf3c366084b0083dff345c3c8c6cf

op_07bcf3c366084b0083dff345c3c8c6cf >> op_ac6d656939964b96928ce14fd10d49a5

op_07bcf3c366084b0083dff345c3c8c6cf >> op_e0061ec3ab2c4cac9d7ca29b5f4b692a
