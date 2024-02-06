import requests
import read_jenkins_config
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
# Make an API request to get job information
response = requests.get(f'{jenkins_url}/api/json', auth=(username, password))
if response.status_code == 200:
   data = response.json()
   jobs = data['jobs']
   if jobs:
       print("List of Jenkins Jobs:")
       for job in jobs:
           print(job['name'])
   else:
       print("No jobs found in Jenkins.")
else:
   print(f"Failed to retrieve job information. Status code: {response.status_code}")
   