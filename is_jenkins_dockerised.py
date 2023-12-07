import requests
def is_jenkins_dockerized(jenkins_url):
   try:
       # Make an HTTP request to Jenkins
       response = requests.get(jenkins_url, auth=('ramarao', 'Jenkins@123')) 
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
# Replace this with your Jenkins server URL
jenkins_url = "http://localhost:8080"
if is_jenkins_dockerized(jenkins_url):
   print("Jenkins is running in a Docker container.")
else:
   print("Jenkins is not running in a Docker container.")