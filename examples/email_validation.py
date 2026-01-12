
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

spark = SparkSession.builder.appName("regex-email-validation").master("local[*]").getOrCreate()

rows = [
    (1, 'john.doe@example.com'),
    (2, 'alice+promo@sub.domain.io'),
    (3, 'bad@domain'),
    (4, 'user@exa_mple.com'),
]

df = spark.createDataFrame(rows, ['id', 'email'])

# Validate using RLIKE via expr
validated = df.withColumn('is_valid', F.expr(f"email RLIKE '{pattern}'"))
validated.show(truncate=False)

spark.stop()
