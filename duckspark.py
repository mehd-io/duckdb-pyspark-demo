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

# Does users who post more stories tend to have higher or lower average scores ?
result = (
    df.filter((col("type") == "story") & (col("by") != "NULL"))
    .groupBy(col("by"))
    .agg(
        avg(col("score")).alias("average_score"),
        count(col("id")).alias("number_of_stories"),
    )
    .filter(col("number_of_stories") > 1)  # Filter users with more than one story
    .orderBy(
        col("number_of_stories").desc(), col("average_score").desc()
    )  # Order by the number of stories first, then by average score
    .limit(10)
)

# show the result
result.show()
