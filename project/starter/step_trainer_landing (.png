CREATE EXTERNAL TABLE IF NOT EXISTS `francisco`.`step_trainer_landing1` (
  `sensorReadingTime` bigint,
  `serialNumber` string,
  `distanceFromObject` float
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'ignore.malformed.json' = 'FALSE',
  'dots.in.keys' = 'FALSE',
  'case.insensitive' = 'TRUE',
  'mapping' = 'TRUE'
)
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://cd0030bucket/step_trainer/'
TBLPROPERTIES ('classification' = 'json');
