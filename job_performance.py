import requests
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
# Replace these with your Jenkins server details and the specific job details
jenkins_url = "http://localhost:8080"
username = "ramarao"
password = "Jenkins@123"
job_name = "your_job_name"
build_number = "your_build_number"
# Call the function to check build duration
check_build_duration(jenkins_url, job_name, build_number, username, password)