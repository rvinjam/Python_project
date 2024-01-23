import requests
import read_jenkins_config
def is_auto_build_configured(jenkins_url, job_name, username, password):
   try:
       # REST API URL for obtaining information about the job configuration
       api_url = f"{jenkins_url.rstrip('/')}/job/{job_name}/config.xml"
       # Make the REST API request to get job configuration
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           job_config = response.text
           # Check if the auto build trigger is configured
           is_auto_build_configured = 'buildOnPullRequest' in job_config
           if is_auto_build_configured:
               print(f"Auto build is configured for job '{job_name}'.")
           else:
               print(f"Auto build is not configured for job '{job_name}'.")
       else:
           print(f"Failed to retrieve job configuration. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
# Example : Testing_java
job_name = input("Enter the job name\n")
# Call the function to check if auto build is configured for a specific job
is_auto_build_configured(jenkins_url, job_name, username, password)