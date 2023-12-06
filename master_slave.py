import requests
def has_master_slave_configuration(jenkins_url):
   try:
       # Make an HTTP request to Jenkins API
       api_url = f"{jenkins_url.rstrip('/')}/computer/api/json"
       response = requests.get(api_url)
       # Check if the response contains information about nodes (slaves)
       data = response.json()
       if 'computer' in data:
           return True
       return False
   except Exception as e:
       print(f"Error: {e}")
       return False
# Replace this with your Jenkins server URL
jenkins_url = "http://localhost:8080"
if has_master_slave_configuration(jenkins_url):
   print("Jenkins has a master-slave configuration.")
else:
   print("Jenkins does not have a master-slave configuration.")