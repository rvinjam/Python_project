import requests
def list_jenkins_nodes(jenkins_url, username, password):
   try:
       # Make an HTTP request to Jenkins API to get information about nodes (slaves)
       api_url = f"{jenkins_url.rstrip('/')}/computer/api/json"
       response = requests.get(api_url, auth=(username, password))
       # Check if the request was successful (HTTP status code 200)
       if response.status_code == 200:
           data = response.json()
           nodes = data.get('computer', [])
           return [node['displayName'] for node in nodes]
       else:
           print(f"Failed to retrieve Jenkins nodes. HTTP Status Code: {response.status_code}")
           return None
   except Exception as e:
       print(f"Error: {e}")
       return None
# Replace these with your Jenkins server URL, username, and password
jenkins_url = "http://localhost:8080"
username = "ramarao"
password = "Jenkins@123"
nodes = list_jenkins_nodes(jenkins_url, username, password)
if nodes:
   print("Jenkins Nodes:")
   for node in nodes:
       print(f"- {node}")
else:
   print("Failed to retrieve Jenkins nodes.")