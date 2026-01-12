# Regex Tutorial with SQL & PySpark

## Goal
Learn practical regex usage in SQL dialects (PostgreSQL/MySQL/BigQuery/Snowflake/Spark SQL) and PySpark DataFrames for validation, extraction, cleaning, and tokenization.

---

## Sample Data
Assume a table `contacts(id INT, email STRING, phone STRING, note STRING)`

Example rows:
```
(1, 'john.doe@example.com', '+91-9876543210', 'Met at #HyderabadTech 2025')
(2, 'alice+promo@sub.domain.io', '9876543210', 'Follow up: invoice-123.45')
(3, 'bad@domain', '12345', 'Tickets: ABC-987 and REF-42')
```

---

## Validation (Email)
PostgreSQL / MySQL 8+ / BigQuery / Snowflake often provide `REGEXP_LIKE`. Spark SQL supports `RLIKE`.

**PostgreSQL (using `~` operator)**
```sql
SELECT id, email,
       (email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$') AS is_valid
FROM contacts;
```

**MySQL 8+**
```sql
SELECT id, email,
       REGEXP_LIKE(email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$') AS is_valid
FROM contacts;
```

**BigQuery**
```sql
SELECT id, email,
       REGEXP_CONTAINS(email, r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$') AS is_valid
FROM `project.dataset.contacts`;
```

**Snowflake**
```sql
SELECT id, email,
       REGEXP_LIKE(email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$') AS is_valid
FROM contacts;
```

**Spark SQL**
```sql
SELECT id, email,
       email RLIKE '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' AS is_valid
FROM contacts;
```

---

## Extraction (Hashtags, Numbers)

**PostgreSQL: `regexp_matches` returns set of matches**
```sql
SELECT id, regexp_matches(note, '#([A-Za-z0-9_]+)', 'g') AS hashtags
FROM contacts;
```

**BigQuery: `REGEXP_EXTRACT`**
```sql
SELECT id, REGEXP_EXTRACT(note, r'#([A-Za-z0-9_]+)') AS first_hashtag
FROM `project.dataset.contacts`;
```

**Snowflake / MySQL: `REGEXP_SUBSTR` / `REGEXP_REPLACE` / `REGEXP_INSTR`**
```sql
SELECT id, REGEXP_SUBSTR(note, '#([A-Za-z0-9_]+)') AS first_hashtag
FROM contacts;
```

**Spark SQL**
```sql
SELECT id, REGEXP_EXTRACT(note, '#([A-Za-z0-9_]+)', 1) AS first_hashtag
FROM contacts;
```

---

## Cleaning (Remove non-digits from phone)

**BigQuery**
```sql
SELECT id, REGEXP_REPLACE(phone, r'[^0-9]', '') AS phone_digits
FROM `project.dataset.contacts`;
```

**MySQL 8+**
```sql
SELECT id, REGEXP_REPLACE(phone, '[^0-9]', '') AS phone_digits
FROM contacts;
```

**Snowflake**
```sql
SELECT id, REGEXP_REPLACE(phone, '[^0-9]', '') AS phone_digits
FROM contacts;
```

**Spark SQL**
```sql
SELECT id, REGEXP_REPLACE(phone, '[^0-9]', '') AS phone_digits
FROM contacts;
```

---

## Tokenization (Split words)

**PostgreSQL: `regexp_split_to_table`**
```sql
SELECT id, regexp_split_to_table(note, '\W+') AS token
FROM contacts;
```

**BigQuery: SPLIT with regex (via normalization)**
```sql
SELECT id, SPLIT(REGEXP_REPLACE(note, r'\W+', ' '), ' ') AS tokens
FROM `project.dataset.contacts`;
```

**Spark SQL**
```sql
SELECT id, SPLIT(REGEXP_REPLACE(note, '[^A-Za-z0-9]+', ' '), ' ') AS tokens
FROM contacts;
```

---

## PySpark DataFrame Examples
```python
from pyspark.sql import functions as F

# Validate email
contacts_df = contacts_df.withColumn(
    "is_valid_email",
    F.expr("email RLIKE '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'")
)

# Extract first hashtag
contacts_df = contacts_df.withColumn(
    "first_hashtag",
    F.regexp_extract("note", r"#([A-Za-z0-9_]+)", 1)
)

# Remove non-digits in phone
contacts_df = contacts_df.withColumn("phone_digits", F.regexp_replace("phone", "[^0-9]", ""))

# Tokenize note into words
contacts_df = contacts_df.withColumn(
    "tokens",
    F.split(F.regexp_replace("note", "[^A-Za-z0-9]+", " "), " ")
)
```

---

## Edge Cases & Tips
- Beware of consecutive dots in emails, Unicode domains, and dialect differences (e.g., `REGEXP_LIKE` vs `RLIKE`).
- Anchor patterns to avoid partial matches.
- Use non-greedy quantifiers where appropriate.

---

## Exercises (with hints)
1. **Extract invoice numbers** like `invoice-123.45` (integer or decimal).
   - Hint: `invoice-(\d+(?:\.\d+)?)`
2. **Validate Indian mobile numbers** with optional country code `+91` and separators.
   - Hint: `^\+?91?[- ]?\d{10}$`
3. **Split notes into tokens** and count hashtag frequency.
   - Hint: `#([A-Za-z0-9_]+)`

---

## Conclusion
Regex in SQL and PySpark enables powerful, set-based text processing directly in your data systems. Combine patterns with other functions for robust pipelines.
