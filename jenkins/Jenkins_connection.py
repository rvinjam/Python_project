import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth
 
jenkins_url = "https://ci-almsmart.dnadevops.hclets.com/"
api_url = jenkins_url + "api/json"
username = "ramarao.vinjam"
password = getpass("Enter your Jenkins password: ")
 
try:
   # response = requests.get(api_url, auth=(username, password))
    response = requests.get(f"{jenkins_url.rstrip('/')}/api/json", auth=HTTPBasicAuth(username, password), verify=True)
    if response.status_code == 200:
        # Connection successful
        print("Connection to Jenkins server successful!")
    else:
        # Connection failed
        print("Failed to connect to Jenkins server. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    # Connection error
    print("An error occurred while connecting to Jenkins server:", str(e))