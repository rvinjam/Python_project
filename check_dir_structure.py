import os
import sys
from xml.dom import ValidationErr

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

  if len(sys.argv) != 2:
    print("Usage: python validate_jenkins_directory_structure.py <jenkins_directory>")
    sys.exit(1)

  jenkins_directory = sys.argv[1]

  try:
    validate_jenkins_directory_structure(jenkins_directory)
  except ValidationErr as e:
    print(e)
    sys.exit(1)

  print("Jenkins directory structure is valid.")

if __name__ == "__main__":
  main()