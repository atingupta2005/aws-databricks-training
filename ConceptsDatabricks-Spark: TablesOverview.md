# Databricks & Spark: Tables Overview

Databricks, built on top of Apache Spark, provides a unified analytics platform for big data analytics and machine learning. One of the core components of the Databricks platform is the ability to work with different types of tables to store and manage data. These tables can be classified into various categories, such as **normal tables**, **Delta tables**, **external tables**, and **managed tables**. Understanding the differences between these types of tables is key to optimizing performance, data management, and resource utilization.

## 1. **Normal Tables**
Normal tables, also referred to as "non-Delta tables," are traditional tables that do not leverage the features of Delta Lake. These tables are typically stored in a variety of formats, such as **Parquet**, **CSV**, or **ORC**.

### Key Characteristics:
- **Data Format**: The underlying data is usually stored in file formats like Parquet, CSV, or JSON.
- **ACID Transactions**: They do not support ACID (Atomicity, Consistency, Isolation, Durability) transactions or other advanced features like schema enforcement, which means data consistency is not guaranteed in case of concurrent writes.
- **Metadata Management**: Metadata is stored in a catalog (e.g., Hive metastore), but lacks robust management features such as version control and auditing.
- **Use Cases**: Best for use cases where ACID compliance is not required or when the data is simple and does not require frequent updates.

### Example in Databricks:
```sql
CREATE TABLE normal_table (
    id INT,
    name STRING
)
USING parquet
LOCATION '/mnt/data/normal_table';
```

## 2. **Delta Tables**
Delta tables are a more advanced version of normal tables in Databricks that leverage **Delta Lake**, which is an open-source storage layer built on top of Apache Spark. Delta tables provide ACID transactions, schema enforcement, and the ability to time-travel to access historical data.

### Key Characteristics:
- **ACID Transactions**: Delta Lake provides ACID properties, ensuring that data is consistent even when there are concurrent writes.
- **Schema Evolution**: Allows for automatic schema evolution when data changes (e.g., new columns are added), which ensures that schema changes do not result in failures or inconsistent states.
- **Time Travel**: Delta Lake provides the ability to query historical versions of data through time travel, allowing users to go back to a specific point in time.
- **Data Versioning**: Each change made to a Delta table is versioned and can be tracked, which is useful for debugging, auditing, and recovering data.
- **Efficient Data Storage**: Delta Lake uses **optimized parquet** storage, offering better performance for read and write operations compared to standard parquet files.
- **Upsert/Deletes**: Delta Lake supports MERGE (upsert), UPDATE, and DELETE operations, which makes it suitable for scenarios requiring mutable datasets.

### Use Cases:
- **Data Lakes**: Storing large volumes of raw data, including unstructured data, that needs to be transformed and processed.
- **Data Warehousing**: Optimized for analytic workloads where historical data is important for analysis.
- **ETL Pipelines**: Delta tables make it easier to build reliable ETL pipelines due to their transactional capabilities.

### Example in Databricks:
```sql
CREATE TABLE delta_table (
    id INT,
    name STRING
)
USING delta
LOCATION '/mnt/data/delta_table';
```

To perform operations like updates, deletes, or merges on a Delta table, you can use SQL or DataFrame API:

```sql
MERGE INTO delta_table AS target
USING updates AS source
ON target.id = source.id
WHEN MATCHED THEN
  UPDATE SET target.name = source.name
WHEN NOT MATCHED THEN
  INSERT (id, name) VALUES (source.id, source.name);
```

## 3. **External Tables**
External tables are tables whose data is stored outside of Databricks' default managed storage (like DBFS or cloud storage) and can reside in other locations like Amazon S3, Azure Blob Storage, or HDFS. These tables are typically used when the data is already stored externally and you want to reference it within Databricks.

### Key Characteristics:
- **Location of Data**: Data can reside in external locations such as Amazon S3, Azure Blob Storage, HDFS, or other file systems. The location is explicitly defined during table creation.
- **Managed Metadata**: Metadata for external tables is managed by the Databricks metastore or an external metastore like Hive, but the underlying data is not managed by Databricks.
- **No Data Deletion**: Dropping an external table only removes the metadata; the data itself remains in the external storage.
- **Flexible Data Source**: You can create external tables over data stored in a variety of formats such as Parquet, CSV, JSON, etc.

### Use Cases:
- **Data Integration**: Useful when integrating with other systems that have data stored externally (e.g., in cloud storage or HDFS).
- **Sharing Data**: External tables can be used to share data across different applications or platforms without moving the actual data.

### Example in Databricks:
```sql
CREATE EXTERNAL TABLE external_table (
    id INT,
    name STRING
)
STORED AS parquet
LOCATION 's3://my-bucket/external-data/';
```

## 4. **Managed Tables**
Managed tables, sometimes called **internal tables**, are tables where both the metadata and the actual data are managed by Databricks. When you create a managed table, Databricks automatically manages both the table's schema and the underlying data files.

### Key Characteristics:
- **Location of Data**: The data for managed tables is stored within the Databricks workspace (DBFS in case of Databricks or cloud-specific storage like AWS S3 or Azure Blob Storage), and the data location is managed by Databricks.
- **Automatic Cleanup**: When you drop a managed table, both the metadata and the data are deleted from the underlying storage. This ensures data is fully cleaned up.
- **Schema and Data Management**: Databricks manages both the schema and the data, making it easy to work with structured and semi-structured data in a centralized way.
- **Optimized for Performance**: Managed tables are optimized for performance within the Databricks ecosystem, as Databricks handles all aspects of storage, file management, and indexing.

### Use Cases:
- **Internal Workloads**: Managed tables are best for internal Databricks workloads where Databricks handles both the data and the metadata.
- **ETL Pipelines**: Managed tables can be used for ETL pipelines where both data and metadata management are required.
  
### Example in Databricks:
```sql
CREATE TABLE managed_table (
    id INT,
    name STRING
)
USING delta;
```

Here, Databricks will automatically manage the storage of the data and metadata for the table.

## 5. **Comparison: Managed vs. External Tables**
| Feature                | Managed Table                            | External Table                          |
|------------------------|------------------------------------------|-----------------------------------------|
| **Data Location**       | Managed by Databricks (DBFS or cloud storage) | External storage (e.g., S3, HDFS, etc.) |
| **Metadata Management** | Managed by Databricks                     | Managed by Databricks or external metastore |
| **Drop Table Behavior** | Both data and metadata are deleted        | Only metadata is deleted; data remains in external location |
| **Use Case**            | For internal storage and management of data | For external data storage integration  |

## 6. **Partitioned Tables**
Partitioning is a technique used to divide a table into smaller, more manageable pieces based on the values of one or more columns. Both **Delta** and **managed tables** can be partitioned to optimize query performance, especially for large datasets.

### Key Characteristics:
- **Partitioning Columns**: Data is divided into partitions based on specific column values, such as **date** or **region**.
- **Improved Performance**: Queries that filter on partitioned columns can benefit from partition pruning, reducing the amount of data read.
- **Metadata**: Partitioning metadata is also stored in the metastore, making partitioned queries efficient.

### Example in Databricks:
```sql
CREATE TABLE partitioned_table (
    id INT,
    name STRING,
    date STRING
)
USING delta
PARTITIONED BY (date)
LOCATION '/mnt/data/partitioned_table';
```

## Conclusion
Databricks supports several types of tables, each serving different use cases depending on the needs of the application. Delta tables, with their ACID compliance, schema evolution, and support for time travel, are particularly well-suited for transactional data workloads. Managed tables are ideal for when you want Databricks to manage both the data and metadata, while external tables are useful for referencing data stored externally without moving it into Databricks-managed storage. Partitioning tables allows you to scale queries efficiently by breaking data into smaller, more manageable pieces.

Choosing the right type of table depends on your workload’s specific requirements, such as performance, data consistency, and how you want to manage storage and metadata.
