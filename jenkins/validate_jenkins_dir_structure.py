import os
import os_check
import sys
from xml.dom import ValidationErr

def get_jenkins_home_directory():
  """Gets the Jenkins home directory.   Returns:     The Jenkins home directory.   """

  jenkins_home_directory = os.environ.get("JENKINS_HOME")
  if jenkins_home_directory is None:
    os_name = os_check.get_platform()
    if os_name == "Windows":
     jenkins_home_directory = "C:\ProgramData\Jenkins\.jenkins"
     print("The Jenkins home directory is not set and using the default directory i.e :", jenkins_home_directory)
     exit(1)
    else :
     jenkins_home_directory = "/var/lib/jenkins"
     print("The Jenkins home directory is not set and using the default directory i.e :", jenkins_home_directory)
     exit(1)
    
  return jenkins_home_directory
def validate_jenkins_directory_structure(jenkins_directory):
  """Validates the Jenkins directory structure.

  Args:
    jenkins_directory: The path to the Jenkins directory.

  Raises:
    ValidationErr: If the Jenkins directory structure is invalid.
  """

  if not os.path.exists(jenkins_directory):
    raise ValidationErr("Jenkins directory does not exist.")

  if not os.path.isdir(jenkins_directory):
    raise ValidationErr("Jenkins directory is not a directory.")

  jenkins_files = [
    "jenkins.yaml",
    "jobs",
    "plugins",
    "secrets",
  ]

  for jenkins_file in jenkins_files:
    if not os.path.exists(os.path.join(jenkins_directory, jenkins_file)):
      raise ValidationErr("Missing Jenkins file {}.".format(jenkins_file))


def main():
  """The main function."""
  jenkins_home_directory = get_jenkins_home_directory()
  print("The Jenkins home directory is:", jenkins_home_directory)
  try:
    validate_jenkins_directory_structure(jenkins_home_directory)
  except ValidationErr as e:
    print(e)
    sys.exit(1)
  


if __name__ == "__main__":
  main()