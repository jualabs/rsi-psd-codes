from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import window
from pyspark.sql.functions import from_unixtime


# create the SparkSession
spark = SparkSession \
    .builder \
    .appName("spark-example-01") \
    .getOrCreate()

# define o esquema de dados do csv a ser lido
fields = [StructField('id', IntegerType(), True), \
    StructField('ts', IntegerType(), True), \
    StructField('value', FloatType(), True), \
    StructField('work_or_load', IntegerType(), True), \
    StructField('plug_id', IntegerType(), True), \
    StructField('household_id', IntegerType(), True), \
    StructField('house_id', IntegerType(), True)]
schema = StructType(fields)
    
# carrega o arquivo csv para o dataframe 'df'
df = spark.read.load("sample-00.csv",
    format="csv", sep=",", schema=schema, header="false")

# converte a coluna 'ts' do time stamp para o formato yyyy-MM-dd HH:mm
# que sera utilizado no agrupamento dos dados
df = df.withColumn('ts', from_unixtime('ts', "yyyy-MM-dd HH:mm")) \

# filtra a coluna 'work_or_load' para pegar apenas as linhas que sao load
df = df.filter(df.work_or_load == 1)

# realiza o agrupamento por casa ('house_id'), comodo ('household_id'), tomada
# ('plug_id') e janela de uma hora ('window('ts', "1 hour")'). Em seguida, realiza
# a agregacao calculando a media da coluna value. 
# Dado que o trabalho (W) = potencia (P) * intervalo de tempo (delta_t), temos que
# ao fazer esta operacao estamos calculando o W em Wh multiplicando a potencia 
# media em uma hora pelo intervalo de 1 hora. Por fim, ordenamos os dados.
# 
# OBS: como temos um intervalo de tempo de uma hora nao e necessario realizar a
# multiplicacao efetivamente.  
df = df.groupBy('house_id', 'household_id', 'plug_id', window('ts', "1 hour")) \
    .agg({"value":"avg"}) \
    .orderBy('house_id', 'household_id', 'plug_id', 'window')

# imprime os dados
df.show()

spark.stop()
