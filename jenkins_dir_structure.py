import os
import jenkins_dir_check

def get_jenkins_directory_structure(jenkins_home_directory):
  """Gets the Jenkins directory structure.

  Args:
    jenkins_home_directory: The path to the Jenkins home directory.

  Returns:
    A list of all the directories in the Jenkins home directory.
  """

  if not os.path.exists(jenkins_home_directory):
    raise ValueError("Jenkins home directory does not exist.")

  return [
      f for f in os.listdir(jenkins_home_directory)
      if os.path.isdir(os.path.join(jenkins_home_directory, f))
  ]

if __name__ == "__main__":
  
  # jenkins_home_directory = jenkins_dir_check.get_jenkins_home_directory()
  jenkins_home_directory = os.environ.get("JENKINS_HOME", "C:\ProgramData\Jenkins\.jenkins")
  print(get_jenkins_directory_structure(jenkins_home_directory))