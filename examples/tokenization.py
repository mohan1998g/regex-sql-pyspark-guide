
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("regex-tokenization").master("local[*]").getOrCreate()

rows = [
    (1, 'Met at #HyderabadTech 2025 with team!'),
    (2, 'Follow up: invoice-123.45, call @ 5 PM.'),
]

df = spark.createDataFrame(rows, ['id', 'note'])

# Normalize separators to spaces, then split
tokens_df = df.withColumn('tokens', F.split(F.regexp_replace('note', '[^A-Za-z0-9]+', ' '), ' '))

tokens_df.show(truncate=False)

spark.stop()
