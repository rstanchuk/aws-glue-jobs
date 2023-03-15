import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


parquet_files_dyf = glueContext.create_dynamic_frame_from_options("s3", {'paths': ["s3://parquet-source-files"]}, format="parquet")

# currentNumPartitions = parquet_files_dyf.getNumPartitions()

parquet_files_dyf_partition_adjusted = parquet_files_dyf.coalesce(1)

# Script generated for node Amazon S3
AmazonS3_node1678892358207 = glueContext.write_dynamic_frame.from_options(
    frame=parquet_files_dyf_partition_adjusted,
    connection_type="s3",
    format="csv",
    connection_options={"path": "s3://csv-target-files", "partitionKeys": []},
    transformation_ctx="AmazonS3_node1678892358207",
)

job.commit()
