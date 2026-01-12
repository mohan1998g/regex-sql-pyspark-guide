# Examples

Runnable PySpark examples demonstrating common regex operations.

## Prerequisites
- Apache Spark (2.4+ or 3.x) with PySpark installed.

## Run
```bash
# From the repository root
pyspark examples/email_validation.py
pyspark examples/extraction_cleaning.py
pyspark examples/tokenization.py

# Or using spark-submit
spark-submit examples/email_validation.py
spark-submit examples/extraction_cleaning.py
spark-submit examples/tokenization.py
```

## Notes
- Adjust `master('local[*]')` in the scripts if you run on a cluster.
- Scripts create small in-memory DataFrames and print results to the console.
