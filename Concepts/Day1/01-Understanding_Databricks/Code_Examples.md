
# 1.4 Practical Code Examples

Examples of connecting Databricks to AWS S3, transforming data, and using Delta Lake.

```python
# Mounting an S3 bucket
dbutils.fs.mount(
  source = "s3a://bucket-name",
  mount_point = "/mnt/s3bucket",
  extra_configs = {"fs.s3a.access.key": "YOUR_ACCESS_KEY", "fs.s3a.secret.key": "YOUR_SECRET_KEY"}
)

# Sample Transformation: Filter and Aggregate Sales Data
df = spark.read.format("csv").option("header", "true").load("/mnt/s3bucket/sales_data.csv")
df_filtered = df.filter(df["sales"] > 1000).groupBy("region").sum("sales")
df_filtered.write.format("delta").save("/mnt/s3bucket/processed_sales")
```

---
