
# 1.1 Reading and Writing Data from S3, Redshift, and Oracle DB

## Working with Amazon S3
1. **Connecting to S3**:
   - **Overview**: Amazon S3 provides scalable object storage suitable for large datasets.
   - **Authentication**: Use IAM roles or AWS credentials securely.
   - **Example**: Mount an S3 bucket to Databricks for streamlined access.
     ```python
     dbutils.fs.mount(
       source="s3a://your-bucket-name",
       mount_point="/mnt/s3bucket",
       extra_configs={"fs.s3a.access.key": "ACCESS_KEY", "fs.s3a.secret.key": "SECRET_KEY"}
     )
     ```

2. **Reading Data from S3**:
   - **Scenario**: Process sales data stored in S3 to analyze customer behavior.
   - **Code**:
     ```python
     df = spark.read.csv("s3a://your-bucket-name/sales-data.csv", header=True, inferSchema=True)
     df.show()
     ```

3. **Writing Data to S3**:
   - **Example**: Save transformed data back to S3 for storage.
     ```python
     df.write.csv("s3a://your-bucket-name/transformed-data", mode="overwrite")
     ```

## Working with Amazon Redshift
1. **Connecting to Redshift**:
   - **Overview**: Redshift serves as a data warehouse, ideal for analytics.
   - **Setup**: Use JDBC to connect Databricks to Redshift.
   - **Code Example**:
     ```python
     jdbc_url = "jdbc:redshift://<endpoint>:5439/<database>"
     properties = {"user": "username", "password": "password"}
     df = spark.read.jdbc(url=jdbc_url, table="table_name", properties=properties)
     ```

2. **Reading Data from Redshift**:
   - **Scenario**: Load sales data from Redshift for quarterly analysis.
   - **Example**:
     ```python
     query = "(SELECT * FROM sales WHERE quarter = 'Q1') AS sales_q1"
     df = spark.read.jdbc(url=jdbc_url, table=query, properties=properties)
     ```

3. **Writing Data to Redshift**:
   - **Example**: Save processed results back into a Redshift table.
     ```python
     df.write.jdbc(url=jdbc_url, table="transformed_sales", mode="append", properties=properties)
     ```

## Working with Oracle DB
1. **Connecting to Oracle DB**:
   - **Setup**: Use the Oracle JDBC driver to connect Databricks to Oracle.
   - **Example**:
     ```python
     jdbc_url = "jdbc:oracle:thin:@//<host>:<port>/<service_name>"
     properties = {"user": "username", "password": "password"}
     df = spark.read.jdbc(url=jdbc_url, table="table_name", properties=properties)
     ```

2. **Reading Data from Oracle**:
   - **Scenario**: Extract customer details for targeted marketing analysis.
   - **Code Example**:
     ```python
     df = spark.read.jdbc(url=jdbc_url, table="customers", properties=properties)
     df.show()
     ```

3. **Writing Data to Oracle**:
   - **Example**: Insert processed data back to Oracle for downstream systems.
     ```python
     df.write.jdbc(url=jdbc_url, table="processed_customers", mode="append", properties=properties)
     ```

---
