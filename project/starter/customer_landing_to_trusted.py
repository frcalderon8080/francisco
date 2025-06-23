import sys
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session


landing_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://your-bucket/customer_landing/"], "recurse": True}
)


trusted_df = landing_df.filter(lambda row: row["shareWithResearchAsOfDate"] is not None)


glueContext.write_dynamic_frame.from_options(
    frame=trusted_df,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://your-bucket/customer_trusted/",
        "partitionKeys": []
    }
)
