import re
import requests
import read_jenkins_config

def check_job_name(job_name):
  """
  Checks if the given job name follows the Jenkins job naming convention.

  Args:
    job_name: The name of the job to check.

  Returns:
    True if the job name follows the convention, False otherwise.
  """

  # The job name must be at least 3 characters long.
  if len(job_name.strip()) < 3:
    print('The job name ', job_name ,' should be at least 3 characters long.')

  # The job name must not contain any spaces.
  if ' ' in job_name.strip():
     print('The job name ', job_name ,' should not contain any spaces.')

  # The job name must start with a lowercase letter.
  if not job_name[0].islower():
     print('The job name ', job_name ,' should start with a lowercase letter.')

  # The job name must only contain lowercase letters, numbers, and hyphens.
  if not re.match(r'[a-z0-9-]+', job_name.strip()):
     print('The job name ', job_name ,' should only contain lowercase letters, numbers, and hyphens.')

# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
# Make an API request to get job information
response = requests.get(f'{jenkins_url}/api/json', auth=(username, password))
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
           check_job_name(job_name)
          
   else:
        print("No jobs found in Jenkins.")
else:
    print(f"Failed to retrieve job information. Status code: {response.status_code}")   