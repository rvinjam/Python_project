import requests
import jenkins_nodes
def list_jobs_on_node(jenkins_url, node_name, username, password):
   try:
       # REST API URL for obtaining information about the node
       api_url = f"{jenkins_url.rstrip('/')}/computer/{node_name}/api/json"
       # Make the REST API request to get information about the node
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           data = response.json()
           # Extract information about the jobs running on the node
           running_jobs = data.get('executors', [])
           if running_jobs:
               print(f"Jobs running on node '{node_name}':")
               for job in running_jobs:
                   job_name = job.get('currentExecutable', {}).get('url', '').split('/')[-3]
                   print(f"- {job_name}")
           else:
               print(f"No jobs running on node '{node_name}'.")
       else:
           print(f"Failed to retrieve node information. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# Replace these with your Jenkins server details and the specific node name
jenkins_url = "http://localhost:8080"
username = "ramarao"
password = "Jenkins@123"
nodes = jenkins_nodes.list_jenkins_nodes(jenkins_url, username, password) 
if nodes:
   print("Jenkins Nodes:")
   for node in nodes:
       node_name = node
       # Call the function to list jobs running on a specific node
       list_jobs_on_node(jenkins_url, node_name, username, password)
else:
   print("Failed to retrieve Jenkins nodes.")

