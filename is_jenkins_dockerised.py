import requests
import read_jenkins_config
def is_jenkins_dockerized(jenkins_url,username,password):
   try:
       # Make an HTTP request to Jenkins
       response = requests.get(jenkins_url, auth=(username, password)) 
       # Check if the 'Server' header contains 'Docker'
       server_header = response.headers.get('Server', '')
       if 'Docker' in server_header:
           return True
       # Check if the response content contains Docker-related information
       if 'docker' in response.text.lower():
           return True
       return False
   except Exception as e:
       print(f"Error: {e}")
       return False
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()

if is_jenkins_dockerized(jenkins_url,username,password):
   print("Jenkins is running in a Docker container.")
else:
   print("Jenkins is not running in a Docker container.")