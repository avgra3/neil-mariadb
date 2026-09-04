# Examples

## Using results from one query in another

Suppose you have a sql query to generate optimize scripts for given tables.

```sql
SELECT CONCAT("OPTIMIZE TABLE ", GROUP_CONCAT(CONCAT(@database,".`",`TABLES`.TABLE_NAME,"` ") SEPARATOR ", "),";") AS "Combined Opimize"
FROM information_schema.`TABLES`
WHERE `TABLES`.TABLE_SCHEMA=@database
AND TABLE_TYPE<>'VIEW'
AND TABLE_NAME NOT LIKE "000%";
```

You could use neil to take the results from that query and then run them as shown below.

```python
from neil import NeilPool, NeilConfig, NeilResult

# SQL from above
sql_generator = "...."

# Normal setup of your pool
config: NeilConfig = NeilConfig(user="admin", password="admin")
runner: NeilPool = NeilPool(conns=config)

generated_sql_query: list[NeilResult] = runner.execute_sql(sql=sql_generator)
if generated_sql_query is None or len(generated_sql_query) == 0:
    return

# Getting our query
actual_query: list[tuple[str | int]] = generated_sql_query.returnedData

# Actually running our query
result: list[NeilResult] = runner.execute_sql(sql="".join([str(i) for i in actual_query]))
```
