import requests
# Replace these variables with your Jenkins server information
jenkins_url = 'http://localhost:8080/'
username = 'admin'
api_token = '111266e5a6cc3260aa208f6355256bec27'  # You can generate this token in Jenkins
# Make an API request to get job information
response = requests.get(f'{jenkins_url}/api/json', auth=(username, api_token))
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
   