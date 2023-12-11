import requests
import read_jenkins_config
def has_master_slave_configuration(jenkins_url):
   try:
       # Make an HTTP request to Jenkins API
       api_url = f"{jenkins_url.rstrip('/')}/computer/api/json"
       print("api_url",api_url)
       response = requests.get(api_url, auth=('ramarao', 'Jenkins@123')) 
       
       # Check if the response contains information about nodes (slaves)
       print("response :",response)
       if response:
            print('Success!')
       else:
            print('An error has occurred.')
            exit(0)
       data = response.json()
       print("Data :",data)
       if 'Slave' in data:
           return True
       return False
   except Exception as e:
       print(f"Error: {e}")
       return False
# Replace this with your Jenkins server URL
jenkins_url, jenkins_username, jenkins_password = read_jenkins_config.read_jenkins_config()
if has_master_slave_configuration(jenkins_url):
   print("Jenkins has a master-slave configuration.")
else:
   print("Jenkins does not have a master-slave configuration.")