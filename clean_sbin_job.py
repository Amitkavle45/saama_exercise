import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import *
from pyspark.sql.functions import *

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

spark = SparkSession.builder.master("local").appName("test").getOrCreate()

df = spark.read.format('csv').option('inferSchema','true').option('header','true').load('s3://sbin_raw/SBIN.csv')
df1 = df.withColumn('Date',to_date('Date','M/d/yyyy'))\
    .withColumn('week_num',weekofyear('Date'))\
    .withColumn('year',year("Date")).withColumnRenamed('Scrip name','Scripname').withColumnRenamed('Adj Close','AdjClose')
#df1.show(truncate=False)
df1.write.format('csv').option('inferSchema','true').option('header','true').save('s3://')
