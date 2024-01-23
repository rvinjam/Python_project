import requests
import jenkins_nodes
import read_jenkins_config
def list_jobs_on_node(jenkins_url, node_name, username, password):
   try:
       # REST API URL for obtaining information about the node
       api_url = f"{jenkins_url.rstrip('/')}/computer/{node_name}/api/json"
       # Make the REST API request to get information about the node
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           data = response.json()
           print(data)
           # Extract information about the jobs running on the node
           isOffline = data.get('offline')
           print(isOffline)
           if not isOffline:
               print(f"Jobs running on node '{node_name}':")
               running_jobs = data.get('executors', [])
               for job in running_jobs:
                   job_name = job.get('currentExecutable', {}).get('url', '').split('/')[-3]
                   print(f"- {job_name}")
           else:
               print(f"No jobs running on node '{node_name}'.")
       else:
           print(f"Failed to retrieve node information. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
nodes = jenkins_nodes.list_jenkins_nodes(jenkins_url, username, password) 
print(nodes)
print("Jenkins Nodes:")
if nodes:
  for node in nodes:
       node_name = node
       # Call the function to list jobs running on a specific node
       list_jobs_on_node(jenkins_url, node_name, username, password)
else:
   print("Failed to retrieve Jenkins nodes.")

