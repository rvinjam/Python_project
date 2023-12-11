import requests
import read_jenkins_config
def get_latest_build_number(jenkins_url, job_name, username, password):
   try:
       # REST API URL for the Jenkins job
       api_url = f"{jenkins_url.rstrip('/')}/job/{job_name}/api/json"
       # Make the REST API request
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           data = response.json()
           latest_build = data.get('lastBuild', {})
           if latest_build is not None:
               latest_build_number = data.get('lastBuild', {}).get('number')
               print(f"Latest build number for job '{job_name}': {latest_build_number}")
               return latest_build_number
           else:
               print(f"No builds found for job '{job_name}'.")
       else:
           print(f"Failed to retrieve build information. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()

response = requests.get(f'{jenkins_url}/api/json', auth=(username, password))
if response.status_code == 200:
   data = response.json()
   jobs = data['jobs']
   if jobs:
       print("List of Jenkins Jobs:")
       for job in jobs:
           print(job['name'])
           job_name = job['name']
           # Call the function to get the latest build number
           get_latest_build_number(jenkins_url, job_name, username, password)
   else:
       print("No jobs found in Jenkins.")
else:
   print(f"Failed to retrieve job information. Status code: {response.status_code}")

