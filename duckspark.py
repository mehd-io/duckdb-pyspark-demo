import os

# Read the environment variable
use_duckdb = os.getenv("USE_DUCKDB", "false").lower() == "true"

if use_duckdb:
    # check current supported functions at https://github.com/duckdb/duckdb/blob/main/tools/pythonpkg/duckdb/experimental/spark/sql/functions.py
    from duckdb.experimental.spark.sql.functions import avg, col, count
    from duckdb.experimental.spark.sql import SparkSession
else:
    from pyspark.sql.functions import avg, col, count
    from pyspark.sql import SparkSession

# create a SparkSession
spark = SparkSession.builder.appName("HackerNewsAuthorStats").getOrCreate()

df = spark.read.parquet("/data/hacker_news_2021_2022.parquet")

# perform the transformation using dataframe style
result = (
    df.filter((col("type") == "story"))
    .groupBy(col("by"))
    .agg(
        avg(col("score")).alias("average_score"),
        count(col("id")).alias("number_of_stories"),
    )
    .orderBy(col("average_score").desc())
    .limit(10)
)

# show the result
result.show()
