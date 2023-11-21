import re

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

if __name__ == '__main__':
  # Get the job name from the user.
  job_name = input('Enter the job name: ')

  # Check if the job name follows the convention.
  if check_job_name(job_name):
    print('The job name follows the convention.')
  else:
    print('The job name does not follow the convention.')