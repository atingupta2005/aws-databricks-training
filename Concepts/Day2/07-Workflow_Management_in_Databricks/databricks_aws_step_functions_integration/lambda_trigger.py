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
