from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
            .appName("Earth") \
            .master("local[3]") \
            .getOrCreate()


kafka_schema = StructType([
    StructField("identifier", StringType()),
    StructField("caption",StringType()),
    StructField("image",StringType()),
    StructField("version",IntegerType()),
    StructField("centroid_coordinates",StructType([
        StructField("lat",StringType()),
        StructField("lon",StringType()),
    ])),
    StructField("dscovr_j2000_position",StructType([
        StructField("x",IntegerType()),
        StructField("y",IntegerType()),
        StructField("z",IntegerType()),
    ])),
    StructField("lunar_j2000_position",StructType([
        StructField("x",IntegerType()),
        StructField("y",IntegerType()),
        StructField("z",IntegerType()),
    ])),
    StructField("sun_j2000_position",StructType([
        StructField("x",IntegerType()),
        StructField("y",IntegerType()),
        StructField("z",IntegerType()),
    ])),
    StructField("attitude_quaternions",StructType([
        StructField("q0",IntegerType()),
        StructField("q1",IntegerType()),
        StructField("q2",IntegerType()),
        StructField("q3",IntegerType()),
    ])),
    StructField("date",StringType()),
    StructField("coords",StructType([
        StructField("centroid_coordinates",StructType([
            StructField("lat",IntegerType()),
            StructField("lon",IntegerType()),
        ])),
        StructField("dscovr_j2000_position",StructType([
        StructField("x",IntegerType()),
        StructField("y",IntegerType()),
        StructField("z",IntegerType()),
        ])),
        StructField("lunar_j2000_position",StructType([
        StructField("x",IntegerType()),
        StructField("y",IntegerType()),
        StructField("z",IntegerType()),
        ])),
        StructField("sun_j2000_position",StructType([
        StructField("x",IntegerType()),
        StructField("y",IntegerType()),
        StructField("z",IntegerType()),
        ])),
        StructField("attitude_quaternions",StructType([
        StructField("q0",IntegerType()),
        StructField("q1",IntegerType()),
        StructField("q2",IntegerType()),
        StructField("q3",IntegerType()),
        ])),
    ])),
])


load_df = spark.read\
            .format("kafka") \
            .option("kafka.bootstrap.servers","localhost:9092") \
            .option("subscribe","earth") \
            .load()

json_df = load_df \
    .select(from_json(col("value").cast("string"), schema=kafka_schema) \
    .alias("earth"))

explode_df = json_df \
    .withColumn("date",to_timestamp(col('earth.date'),'yyyy-MM-dd HH:mm:ss')) \
    .select(col("earth.identifier").alias("identifier"),
            col("earth.caption").alias("caption"),
            col("earth.image").alias("image"),
            col("earth.centroid_coordinates.lat").alias("lat"),
            col("earth.centroid_coordinates.lon").alias("lon"),
            col("earth.date").alias("my_date"),
    ) \

# refine_df = explode_df \
#     .withColumn("date",to_timestamp(col('my_date'),'yyyy-MM-dd HH:mm:ss'))

# final_df = explode_df  \
#     .withColumn("day",dayofmonth("date")) \
#     .withColumn("month",month("date"))  \
#     .withColumn("year",year("date"))
# url = "https://epic.gsfc.nasa.gov/archive/enhanced"

explode_df.show()