
# 1.2 Accessing Data from Azure Data Lake Storage (ADLS) in a Multi-Cloud Setup

## Multi-Cloud Integration with ADLS
1. **Connecting to ADLS**:
   - **Overview**: Azure Data Lake Storage provides scalable storage for big data and integrates well with Databricks.
   - **Authentication**: Use Service Principal credentials or managed identities.
   - **Code Example**:
     ```python
     spark.conf.set("fs.azure.account.key.<storage_account_name>.dfs.core.windows.net", "your-access-key")
     df = spark.read.parquet("abfss://<container>@<storage_account>.dfs.core.windows.net/path/to/data")
     ```

2. **Reading Data from ADLS**:
   - **Scenario**: A company combines data from AWS and Azure to generate a unified report.
   - **Example**:
     ```python
     df = spark.read.parquet("abfss://data@storage_account.dfs.core.windows.net/sales-data")
     df.show()
     ```

3. **Writing Data to ADLS**:
   - **Example**: Save transformed data for multi-cloud analytics.
     ```python
     df.write.parquet("abfss://analytics@storage_account.dfs.core.windows.net/transformed-data", mode="overwrite")
     ```

## Best Practices for Multi-Cloud Data Access
1. **Establish Security Controls**:
   - Use strong authentication mechanisms to ensure secure access across clouds.

2. **Optimize Data Transfer**:
   - Minimize data movement by processing as close to the data source as possible.

3. **Enable Cross-Cloud Analytics**:
   - Access data from both AWS and Azure within Databricks for centralized analysis.

---
