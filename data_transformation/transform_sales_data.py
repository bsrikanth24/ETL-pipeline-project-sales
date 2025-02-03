from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, expr
import os  # Import necessário para manipular diretórios
import findspark

findspark.init("C:/spark")  # Substitua pelo caminho onde você instalou o Spark

# Inicializar SparkSession
spark = SparkSession.builder \
    .appName("Transformação de Dados de Vendas") \
    .config("spark.hadoop.native.lib", "false") \
    .config("spark.sql.parquet.output.committer.class", "org.apache.parquet.hadoop.ParquetOutputCommitter") \
    .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2") \
    .config("spark.hadoop.mapreduce.fileoutputcommitter.marksuccessfuljobs", "false") \
    .config("spark.sql.sources.commitProtocolClass", "org.apache.spark.internal.io.DummyWriteTaskCommitProtocol") \
    .getOrCreate()

# Caminho do arquivo de entrada
input_path = "C:/Users/cezar/OneDrive - MSFT/Área de Trabalho/GITHUB/etl-pipeline-projeto-vendas/sales_data.csv"

# Carregar o arquivo CSV
sales_df = spark.read.csv(input_path, header=True, inferSchema=True)

# Exibir os dados carregados
print("Dados carregados:")
sales_df.show()

# Transformações:
sales_df = sales_df.withColumn("total_revenue", round(col("quantity") * col("price_per_unit"), 2))
sales_df = sales_df.withColumn(
    "price_category",
    expr("CASE WHEN price_per_unit < 20 THEN 'Low' WHEN price_per_unit < 50 THEN 'Medium' ELSE 'High' END")
)

# Exibir os dados transformados
print("Dados transformados:")
sales_df.show()

# Caminho do arquivo de saída
output_dir = "transformed_data"
output_path = os.path.join(output_dir, "transformed_sales_data.csv")

# Criar o diretório de saída, se não existir
os.makedirs(output_dir, exist_ok=True)

# Converter para Pandas e salvar
sales_df_pandas = sales_df.toPandas()
sales_df_pandas.to_csv(output_path, index=False)

print(f"Dados salvos em {output_path}")

# Encerrar a SparkSession
spark.stop()
