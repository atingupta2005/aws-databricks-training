
# 1.1 Cluster Types and Autoscaling Options

## Overview of Cluster Types
1. **Standard Clusters**:
   - Designed for individual users or small groups to run workloads that don't require concurrency.
   - **Example**: Used by data scientists working on machine learning models or data exploration.

2. **High Concurrency Clusters**:
   - Supports multiple concurrent tasks with optimized resource sharing, suitable for interactive workloads with many users.
   - **Example**: Teams running interactive analytics or SQL queries benefit from high concurrency clusters.

3. **Single Node Clusters**:
   - Used primarily for single-user workloads, such as development and testing.
   - **Example**: A data engineer testing ETL scripts in a contained environment.

## Autoscaling Options
1. **Enabled Autoscaling**:
   - Databricks can automatically scale clusters based on workload demands, adjusting the number of nodes as needed.
   - **Use Case**: A business processing daily sales data in real-time may enable autoscaling to handle peak loads efficiently.
   - **Configuration**: Set a minimum and maximum number of nodes to control scaling limits.

2. **Disabled Autoscaling**:
   - Fixed clusters, where the number of nodes does not change. Useful for predictable workloads where resources remain constant.
   - **Example**: A model training pipeline that consistently uses the same resources can use a fixed cluster to minimize cost.

---

