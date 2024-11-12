
# Databricks and AWS Step Functions Integration: Case Study

## Objective

This case study demonstrates how to integrate **Databricks** with **AWS Step Functions** for orchestrating complex workflows. We will use AWS Step Functions to trigger Databricks jobs that perform data processing (ETL) and machine learning tasks.

## Use Case

### 1. Preprocessing Data (ETL)
- Trigger a Databricks job that reads raw data from **Amazon S3**, processes it (cleaning, transformation), and writes it back to S3.

### 2. Model Training
- Trigger a Databricks job that trains a machine learning model using the processed data.

### 3. Model Evaluation
- Trigger a Databricks job that evaluates the trained model and stores the results in **Amazon S3**.

## Architecture Overview

The architecture involves the following components:
- **AWS Step Functions**: Orchestrates the workflow between different Databricks jobs.
- **AWS Lambda**: Invokes Databricks REST API to trigger Databricks jobs based on the parameters provided by Step Functions.
- **Databricks**: Executes notebooks for ETL, model training, and model evaluation.
- **Amazon S3**: Stores the input data, processed data, trained models, and evaluation results.
- **IAM Roles**: Provide the necessary permissions for Step Functions, Lambda, and Databricks.

## Databricks Job Trigger Lambda Function

The Lambda function triggers Databricks jobs using the Databricks REST API. It accepts parameters like `notebook_path`, `cluster_id`, and `job_params`, and dynamically invokes the relevant Databricks job.

### Lambda Function Code (lambda_trigger.py)

```python
import json
import requests

def lambda_handler(event, context):
    # Databricks API URL (the same URL for all jobs)
    databricks_url = "https://<databricks-instance>/api/2.0/jobs/run-now"
    
    # Databricks token for authentication
    databricks_token = "Bearer <your-databricks-token>"
    
    # Extract parameters passed by Step Functions
    notebook_path = event['notebook_path']
    cluster_id = event['cluster_id']
    job_params = event['job_params']
    
    # Construct the payload for Databricks API
    payload = {
        "notebook_task": {
            "notebook_path": notebook_path
        },
        "cluster_id": cluster_id,
        "notebook_params": job_params
    }
    
    # Headers for the API request
    headers = {'Authorization': databricks_token}
    
    # Send POST request to Databricks API to trigger the job
    response = requests.post(databricks_url, json=payload, headers=headers)
    
    # Handle response and return appropriate status
    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Databricks job triggered successfully')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to trigger Databricks job: {response.text}")
        }
}
```

## Final Steps for Integration

1. **Deploy Lambda**: Deploy the Lambda function (`lambda_trigger.py`) in AWS Lambda.
2. **Create Step Functions State Machine**: Use the Step Functions Console or AWS CLI to create the state machine.
3. **Configure Permissions**: Ensure IAM roles are configured correctly for Lambda, Step Functions, and Databricks.
4. **Test Workflow**: Test the entire workflow by triggering the Step Functions state machine, which will invoke the Lambda function and trigger Databricks jobs.

