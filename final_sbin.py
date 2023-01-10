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

df2 = df1.groupBy('week_num','year').agg(min(col('Date')).alias('st_date'),\
                                         max(col('Date')).alias('end_date'),\
                                         max(col('High')).alias('High'),\
                                         min(col('Low')).alias('Low'),\
                                         avg(col('AdjClose')).alias('Adj_close'),\
                                         sum(col('Volume')).alias('Volume'))
#df2.show(truncate=False)

sbin = df1.select('Scripname','Open','Date').join(df2,df2.st_date==df1.Date,'inner')\
    .drop(df1.Date).join(df1.select('Date','Close'),df1.Date==df2.end_date,'inner')\
    .select('Scripname','week_num','st_date','end_date','Open','High','Low','Close','Adj_close','Volume')\
    .orderBy('st_date')

#sbin.show()
sbin.coalesce(1).write.format('csv').option('inferSchema','true').option('header','true').save('s3://new_sbin/')


#datasink2 = glueContext.write_dynamic_frame.from_options(frame = applymapping1, connection_type = "s3", connection_options = {"path": "s3://new_sbin/"}, format = "csv", transformation_ctx = "datasink2")
job.commit()