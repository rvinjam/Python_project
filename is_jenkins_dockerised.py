import subprocess

def is_jenkins_dockerised():
  """Returns True if Jenkins is dockerised, False otherwise."""
  output = subprocess.check_output(["docker", "ps"])
  
  print(output)
  return 'jenkins' in output

if __name__ == '__main__':
  if is_jenkins_dockerised():
    print('Jenkins is dockerised')
  else:
    print('Jenkins is not dockerised')