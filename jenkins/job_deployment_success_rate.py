import requests
import read_jenkins_config
def deployment_success_rate(jenkins_url, job_name, username, password):
   try:
       # REST API URL for obtaining information about the job
       api_url = f"{jenkins_url.rstrip('/')}/job/{job_name}/api/json"
       # Make the REST API request to get job information
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           job_info = response.json()
           # Check the build statuses and calculate deployment success rate
           total_builds = len(job_info['builds'])
           successful_deployments = sum(1 for build in job_info['builds'] if build['result'] == 'SUCCESS')
           success_rate = (successful_deployments / total_builds) * 100 if total_builds > 0 else 0
           print(f"Deployment Success Rate for job '{job_name}': {success_rate:.2f}%")
       else:
           print(f"Failed to retrieve job information. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
# Call the function to calculate deployment success rate for a specific job
response = requests.get(f'{jenkins_url}/api/json', auth=(username, password))
if response.status_code == 200:
   data = response.json()
   jobs = data['jobs']
   print("List of Jenkins Jobs:")
   if jobs:
       for job in jobs:
           print(job['name'])
           job_name = job['name']
           # Call the function to count aborted builds for a specific job
           deployment_success_rate(jenkins_url, job_name, username, password)
   else:
        print("No jobs found in Jenkins.")  
else:
   print(f"Failed to retrieve job information. Status code: {response.status_code}")