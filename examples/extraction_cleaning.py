
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("regex-extraction-cleaning").master("local[*]").getOrCreate()

rows = [
    (1, '+91-9876543210', 'Met at #HyderabadTech 2025'),
    (2, '987 654 3210', 'Follow up: invoice-123.45 and #FollowUp'),
    (3, '(040) 123-4567', 'Tickets: ABC-987 and REF-42 #support'),
]

df = spark.createDataFrame(rows, ['id', 'phone', 'note'])

# Clean phone to digits only
cleaned = df.withColumn('phone_digits', F.regexp_replace('phone', '[^0-9]', ''))

# Extract first hashtag
extracted = cleaned.withColumn('first_hashtag', F.regexp_extract('note', r'#([A-Za-z0-9_]+)\b', 1))

extracted.show(truncate=False)

spark.stop()
