### **DBFS in AWS

#### **1. What is DBFS?**
Databricks File System (**DBFS**) is a distributed file system that abstracts the underlying cloud storage (Amazon S3 for AWS). It allows you to interact with files using simple paths like `/dbfs/` in Databricks notebooks.

#### **2. Storage Location**
- Files created in DBFS are stored in **Amazon S3**, but accessed through the `/dbfs/` path in Databricks.
- Databricks automatically manages the S3 buckets for DBFS.

#### **3. Example Workspace and Cluster**

- **Workspace Name**: `my-databricks-workspace`
- **Cluster Name**: `my-cluster-01`

#### **4. Example DBFS File Path**

- **DBFS Path**: `/dbfs/tmp/myfile.txt`
- **Actual S3 Path**: `s3://databricks-prod-my-databricks-workspace-us-east-1/dbfs/tmp/myfile.txt`

#### **5. Writing to DBFS (Example Code)**

```python
# Writing a file to DBFS (e.g., /tmp/myfile.txt)
dbutils.fs.put("/dbfs/tmp/myfile.txt", "Sample data.", overwrite=True)
```

#### **6. Accessing Files in DBFS (Example Code)**

```python
# Reading the file from DBFS
with open("/dbfs/tmp/myfile.txt", "r") as f:
    content = f.read()
    print(content)
```
