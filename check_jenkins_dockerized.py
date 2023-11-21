import subprocess

def check_jenkins_dockerized():
  """Checks if Jenkins is Dockerized or not.

  Returns:
    True if Jenkins is Dockerized, False otherwise.
  """

  output = subprocess.check_output(['docker', 'ps'])
  if 'jenkins' in output:
    return True
  else:
    return False

if __name__ == '__main__':
  if check_jenkins_dockerized():
    print('Jenkins is Dockerized.')
  else:
    print('Jenkins is not Dockerized.')