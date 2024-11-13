In Databricks, you can view information about who ran a job, including the user who triggered it, in the **Job Run History** section. Here's how to check this information:

1. **Navigate to Jobs:**
   - Go to your Databricks workspace.
   - In the left sidebar, click on **Jobs**.

2. **Select the Job:**
   - Find the job for which you want to see the execution details.
   - Click on the job name to view its details.

3. **Check the Run History:**
   - On the job details page, you'll see a **Run History** tab.
   - This shows a list of all the past runs of the job, including their status (e.g., succeeded, failed).
   
4. **View the Triggering User:**
   - For each run in the history, you'll see a column labeled **Triggered by**. This indicates who triggered the job (the user who initiated the run).

If you're using the **Job API** (REST API), you can also retrieve details about job runs, including the user who triggered the run, by querying the `/api/2.0/jobs/runs/list` endpoint.

Let me know if you need more details or instructions on how to use the API for this!