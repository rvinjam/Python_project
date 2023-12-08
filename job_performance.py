import requests
import find_latest_build_number

def check_build_duration(jenkins_url, job_name, build_number, username, password):
   try:
       api_url = f"{jenkins_url.rstrip('/')}/job/{job_name}/{build_number}/api/json"
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           data = response.json()
           duration = data.get('duration')
           if duration is not None:
               print(f"Build {build_number} for job '{job_name}' took {duration / 1000:.2f} seconds.")
           else:
               print(f"Error: Unable to retrieve build duration for job '{job_name}' and build number {build_number}.")
       else:
           print(f"Failed to retrieve build information. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
jenkins_url = "http://localhost:8080"
username = "ramarao"
password = "Jenkins@123"
response = requests.get(f'{jenkins_url}/api/json', auth=(username, password))
if response.status_code == 200:
   data = response.json()
   jobs = data['jobs']
   print("List of Jenkins Jobs:")
   if jobs:
       for job in jobs:
           print(job['name'])
           job_name = job['name']
           # Call the function to get the latest build number
           build_number = find_latest_build_number.get_latest_build_number(jenkins_url, job_name, username, password)
           # Call the function to check build duration
           check_build_duration(jenkins_url, job_name, build_number, username, password)
   else:
       print("No jobs found in Jenkins.")
else:
   print(f"Failed to retrieve job information. Status code: {response.status_code}")
