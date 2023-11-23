import re
import requests

def check_job_name(job_name):
  """
  Checks if the given job name follows the Jenkins job naming convention.

  Args:
    job_name: The name of the job to check.

  Returns:
    True if the job name follows the convention, False otherwise.
  """

  # The job name must be at least 3 characters long.
  if len(job_name) < 3:
    return False

  # The job name must not contain any spaces.
  if ' ' in job_name:
    return False

  # The job name must start with a lowercase letter.
  if not job_name[0].islower():
    return False

  # The job name must only contain lowercase letters, numbers, and hyphens.
  if not re.match(r'[a-z0-9-]+', job_name):
    return False

  return True
# Replace these variables with your Jenkins server information
jenkins_url = 'http://localhost:8080/'
username = 'admin'
api_token = '111266e5a6cc3260aa208f6355256bec27'  # You can generate this token in Jenkins
# Make an API request to get job information
response = requests.get(f'{jenkins_url}/api/json', auth=(username, api_token))
if response.status_code == 200:
   data = response.json()
   jobs = data['jobs']
   job_name = ""
   if jobs:
       print("List of Jenkins Jobs:")
       for job in jobs:
           print(job['name'])
          # Get the job name from the user.
           job_name = job['name']

          # Check if the job name follows the convention.
           if check_job_name(job_name):
            print('The job name ', job_name ,' follows the convention.')
           else:
            print('The job name ', job_name ,' does not follows the convention.')
   else:
        print("No jobs found in Jenkins.")
else:
    print(f"Failed to retrieve job information. Status code: {response.status_code}")   