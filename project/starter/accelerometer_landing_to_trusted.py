
customer_df = glueContext.create_dynamic_frame.from_catalog(
    database="your_database", table_name="customer_trusted"
)

accel_df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://your-bucket/accelerometer_landing/"], "recurse": True}
)


joined_df = accel_df.join(
    paths1=["user"],
    frame2=customer_df,
    paths2=["email"]
)


projected_df = joined_df.drop_fields(["email", "serialNumber", "shareWithResearchAsOfDate", ...])


glueContext.write_dynamic_frame.from_options(
    frame=projected_df,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://your-bucket/accelerometer_trusted/"}
)
