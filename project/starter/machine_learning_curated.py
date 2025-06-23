
step_df = glueContext.create_dynamic_frame.from_catalog(
    database="your_database", table_name="step_trainer_trusted"
)
accel_df = glueContext.create_dynamic_frame.from_catalog(
    database="your_database", table_name="accelerometer_trusted"
)

joined_df = step_df.join(
    paths1=["sensorReadingTime"],
    frame2=accel_df,
    paths2=["timestamp"]
)


anonymized_df = joined_df.drop_fields(["email", "user"])

glueContext.write_dynamic_frame.from_options(
    frame=anonymized_df,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://your-bucket/machine_learning_curated/"}
)
