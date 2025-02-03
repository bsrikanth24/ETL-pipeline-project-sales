import os
import pandas as pd
from google.cloud import bigquery

# Configuração do caminho para o arquivo de chave JSON
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key.json"

# Função para carregar os dados transformados no BigQuery
def load_to_bigquery(file_path, dataset_id, table_name):
    """
    Carrega um arquivo transformado (CSV) para o BigQuery.

    Args:
        file_path (str): Caminho para o arquivo de dados transformados.
        dataset_id (str): ID do dataset no BigQuery.
        table_name (str): Nome da tabela no BigQuery.
    """
    # Inicializa o cliente BigQuery
    client = bigquery.Client()

    # Lê os dados do arquivo CSV
    df = pd.read_csv(file_path)

    # Configuração do job
    table_id = f"{dataset_id}.{table_name}"
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Substitui dados existentes
        autodetect=True,  # Detecta tipos automaticamente
    )

    # Carrega os dados
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Aguarda a conclusão

    # Verifica o status
    table = client.get_table(table_id)
    print(f"Dados carregados com sucesso na tabela {table_id}. Total de linhas: {table.num_rows}")

# Exemplo de uso
if __name__ == "__main__":
    file_path = "data_transformation/transformed_data/transformed_sales_data.csv"  # Caminho para o arquivo transformado
    dataset_id = "pipeline-projeto-vendas.sales_data"  # Substitua pelo ID do seu dataset no BigQuery
    table_name = "transformed_sales_data"  # Nome da tabela no BigQuery
    load_to_bigquery(file_path, dataset_id, table_name)
