# Example ETL Notebook for Databricks

df = spark.read.csv("s3://your-bucket-name/raw-data.csv", header=True, inferSchema=True)
df_cleaned = df.filter(df['column_name'].isNotNull())
df_cleaned.write.parquet("s3://your-bucket-name/processed-data/")
