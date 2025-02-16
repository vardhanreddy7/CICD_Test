from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.appName("PySparkSQLExample").getOrCreate()

data = [
    Row(id=1, name="Alice", age=25, city="New York"),
    Row(id=2, name="Bob", age=30, city="Los Angeles"),
    Row(id=3, name="Charlie", age=35, city="Chicago")
]

df = spark.createDataFrame(data)

df.createOrReplaceTempView("people")

result_df = spark.sql("select id, name, age FROM people WHERE age > 28")
