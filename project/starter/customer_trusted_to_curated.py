# Join customer_trusted with accelerometer_trusted by email/user
customer_df = glueContext.create_dynamic_frame.from_catalog(
    database="your_database", table_name="customer_trusted"
)
accel_df = glueContext.create_dynamic_frame.from_catalog(
    database="your_database", table_name="accelerometer_trusted"
)

joined_df = customer_df.join(
    paths1=["email"],
    frame2=accel_df,
    paths2=["user"]
)

# Only keep customer fields
curated_df = joined_df.drop_fields(["user", "x", "y", "z", "timestamp"])

# Write curated customer
glueContext.write_dynamic_frame.from_options(
    frame=curated_df,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://your-bucket/customer_curated/"}
)
