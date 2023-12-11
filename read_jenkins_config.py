import configparser
import requests
def read_jenkins_config(file_path='jenkins_config.properties'):
   config = configparser.ConfigParser()
   config.read(file_path)
   jenkins_url = config.get('jenkins', 'jenkins_url')
   jenkins_username = config.get('jenkins', 'username')
   jenkins_password = config.get('jenkins', 'password')
   return jenkins_url, jenkins_username, jenkins_password
def check_jenkins_connection(jenkins_url, username, password):
   try:
       # Example: Making a simple GET request to Jenkins
       response = requests.get(f"{jenkins_url.rstrip('/')}/api/json", auth=(username, password))
       if response.status_code == 200:
           print("Connection to Jenkins successful.")
       else:
           print(f"Failed to connect to Jenkins. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# Read Jenkins configuration from properties file
jenkins_url, jenkins_username, jenkins_password = read_jenkins_config()
# Call the function to check Jenkins connection
check_jenkins_connection(jenkins_url, jenkins_username, jenkins_password)