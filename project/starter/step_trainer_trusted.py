
step_df = glueContext.create_dynamic_frame.from_catalog(
    database="your_database", table_name="step_trainer_landing"
)
cust_df = glueContext.create_dynamic_frame.from_catalog(
    database="your_database", table_name="customer_curated"
)

joined_df = step_df.join(
    paths1=["serialNumber"],
    frame2=cust_df,
    paths2=["serialNumber"]
)


glueContext.write_dynamic_frame.from_options(
    frame=joined_df,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://your-bucket/step_trainer_trusted/"}
)
