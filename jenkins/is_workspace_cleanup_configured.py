import requests
import read_jenkins_config
def is_workspace_cleanup_configured(jenkins_url, job_name, username, password):
   try:
       # REST API URL for obtaining information about the job configuration
       api_url = f"{jenkins_url.rstrip('/')}/job/{job_name}/config.xml"
       # Make the REST API request to get job configuration
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           job_config = response.text
           # Check if the workspace cleanup option is configured
           is_cleanup_configured = '<class>hudson.plugins.ws__cleanup.WsCleanup</class>' in job_config
           if is_cleanup_configured:
               print(f"Workspace cleanup is configured for job '{job_name}'.")
           else:
               print(f"Workspace cleanup is not configured for job '{job_name}'.")
       else:
           print(f"Failed to retrieve job configuration. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
# Example : Testing_java
job_name = input("Enter the job name\n")
# Call the function to check if workspace cleanup is configured for a specific job
is_workspace_cleanup_configured(jenkins_url, job_name, username, password)