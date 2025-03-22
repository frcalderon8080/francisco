CREATE EXTERNAL TABLE stedi_data_lake.customer_trusted (
  serialnumber STRING,
  sharewithpublicasofdate BIGINT,
  birthday STRING,
  registrationdate BIGINT,
  sharewithresearchasofdate BIGINT,
  customername STRING,
  email STRING,
  lastupdatedate BIGINT,
  phone STRING,
  sharewithfriendsasofdate BIGINT
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json' = 'FALSE',
  'dots.in.keys' = 'FALSE',
  'case.insensitive' = 'TRUE',
  'mapping' = 'TRUE'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://stedi-data-lake-kam/customer/trusted/'
TBLPROPERTIES ('classification' = 'json');
