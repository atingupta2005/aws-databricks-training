# Connecting to an On-Premises SQL Server from AWS Databricks

## 1. Introduction

AWS Databricks allows seamless access to cloud-native and on-premises databases. When working with an on-premises SQL Server, establishing a secure and efficient connection is essential, as it requires configuring networking between AWS and the on-premises environment. This guide explains how to set up and configure AWS Databricks to connect securely to an on-premises SQL Server.

---

## 2. Network Prerequisites and Requirements

Connecting from AWS Databricks to an on-premises SQL Server requires:

- A **network connection** between the AWS Virtual Private Cloud (VPC) where Databricks is hosted and the on-premises network.
- A **SQL Server JDBC driver** installed on the Databricks cluster.
- Proper **security configurations** on both AWS and the on-premises SQL Server, including firewall settings.

---

## 3. Setting Up AWS Networking

There are several options for creating a secure network connection from AWS to an on-premises environment:

### VPC Peering

**VPC Peering** allows private connections between two VPCs. It’s commonly used for AWS-to-AWS connections but may not be the best choice for connecting on-premises databases.

### VPN Connection

1. **Site-to-Site VPN**: Use AWS Site-to-Site VPN to establish a secure IPsec connection between your on-premises network and the AWS VPC.
   - **Requirements**: A compatible VPN device on-premises.
   - **Configuration**: Set up the VPN through the AWS Management Console, following the [AWS Site-to-Site VPN Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

2. **Client VPN**: If you only need secure connectivity for specific users or applications, consider using AWS Client VPN.

### AWS Direct Connect

For high-performance, low-latency connections, **AWS Direct Connect** offers a dedicated line between AWS and on-premises environments. This is often more expensive but provides higher bandwidth and reliability.

---

## 4. Configuring Security Groups and Access

Once networking is configured, ensure security settings allow communication between Databricks and SQL Server:

1. **Security Groups**:
   - Create an AWS security group with inbound rules to allow traffic from the on-premises IP range or VPN IP range on the **SQL Server port** (default is TCP port `1433`).

2. **Firewall Rules** on SQL Server:
   - Open the SQL Server port (`1433`) on the firewall in the on-premises environment to allow inbound traffic from the AWS VPC or VPN IP range.

3. **Network ACLs**:
   - Configure Network ACLs in AWS to allow communication between the Databricks VPC subnet and the on-premises IP range.

---

## 5. Setting Up Databricks Cluster with SQL Server Drivers

To connect to SQL Server, ensure your Databricks cluster has the **SQL Server JDBC driver** installed.

1. **Download the SQL Server JDBC Driver**:
   - Download the latest Microsoft JDBC Driver for SQL Server from [Microsoft’s website](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server).

2. **Upload the JDBC Driver to Databricks**:
   - Use the Databricks UI to upload the JDBC `.jar` file to a DBFS location or directly to the Databricks cluster.

3. **Attach the JDBC Driver to the Cluster**:
   - Go to **Clusters > Libraries** in the Databricks UI, and attach the JDBC driver `.jar` to your cluster.

---

## 6. Connecting to SQL Server from Databricks

### Defining Connection Properties

Define the connection properties, including the SQL Server endpoint, database name, user credentials, and other relevant configurations.

```python
# Define connection properties
jdbc_hostname = "your-onprem-sqlserver-hostname"
jdbc_port = "1433"  # Default SQL Server port
database = "your_database_name"
username = "your_username"
password = "your_password"

# Construct the JDBC URL
jdbc_url = f"jdbc:sqlserver://{jdbc_hostname}:{jdbc_port};databaseName={database}"

# Connection properties
connection_properties = {
    "user": username,
    "password": password,
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}
```

### Connecting with PySpark

Using the connection properties, you can now read from or write to the SQL Server database in Databricks.

#### Reading Data from SQL Server

```python
# Reading data from SQL Server into a Spark DataFrame
sql_server_df = spark.read.jdbc(url=jdbc_url, table="your_table_name", properties=connection_properties)
sql_server_df.show(5)
```

#### Writing Data to SQL Server

```python
# Writing data from a Spark DataFrame to SQL Server
sample_data = [(1, "John Doe", 30), (2, "Jane Smith", 25)]
columns = ["id", "name", "age"]
df = spark.createDataFrame(sample_data, columns)

df.write.jdbc(url=jdbc_url, table="your_table_name", mode="overwrite", properties=connection_properties)
```
