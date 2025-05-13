from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# # Garante que o Airflow encontre o main.py
# sys.path.append(os.path.abspath("."))
# Adiciona o diretório raiz ao sys.path para importar do main

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

# Importa as funções diretamente do main
from main import (
    extrair_dados_breweries,
    converter_json_para_csv,
    transformar_dados,
    agregar_dados
)

default_args = {
    "owner": "Lucas L. Lima",
    "start_date": datetime(2025, 5, 9),
    "retries": 1
}

with DAG(
    dag_id="brewery_pipeline",
    default_args=default_args,
    schedule_interval='0 9 * * *',
    catchup=False,
    tags=["Brewery", "ETL", "Pipeline"]
) as dag:

    extrair = PythonOperator(
        task_id="extrair_dados",
        python_callable=extrair_dados_breweries,
    )

    converter = PythonOperator(
        task_id="converter_para_csv",
        python_callable=converter_json_para_csv,
    )

    transformar = PythonOperator(
        task_id="transformar_dados",
        python_callable=transformar_dados,
    )

    agregar = PythonOperator(
        task_id="agregar_dados",
        python_callable=agregar_dados,
    )

    # Definindo ordem de execução
    extrair >> converter >> transformar >> agregar
