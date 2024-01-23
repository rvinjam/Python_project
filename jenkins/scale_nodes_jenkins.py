import requests
import read_jenkins_config
def scale_nodes(jenkins_url, username, password, node_name, num_nodes_to_add=0, num_nodes_to_remove=0):
   try:
       # REST API URL for obtaining information about the Jenkins master
       api_url = f"{jenkins_url.rstrip('/')}/computer/api/json"
       # Make the REST API request to get information about the Jenkins master
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           computer_info = response.json()
           # Identify the Jenkins master(Built-In Node)
           master_node = next((node for node in computer_info['computer'] if node['displayName'] == 'Built-In Node'), None)
           if master_node:
               # Get the current number of executors (nodes) on the master
               current_executors = master_node['numExecutors']
               # Calculate the new number of executors
               new_executors = current_executors + num_nodes_to_add - num_nodes_to_remove
               # Update the number of executors on the master
               update_url = f"{jenkins_url.rstrip('/')}/computer/(master)/numExecutors/{new_executors}"
               update_response = requests.post(update_url, auth=(username, password))
               if update_response.status_code == 200:
                   print(f"Nodes scaled successfully. New number of nodes: {new_executors}")
               else:
                   print(f"Failed to scale nodes. HTTP Status Code: {update_response.status_code}")
           else:
               print("Master node not found in Jenkins computer information.")
       else:
           print(f"Failed to retrieve Jenkins computer information. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
node_name = "Built-In Node"  # Master node in this example
num_nodes_to_add = 2  # Number of nodes to add
num_nodes_to_remove = 1  # Number of nodes to remove
# Call the function to scale the number of nodes
scale_nodes(jenkins_url, username, password, node_name, num_nodes_to_add, num_nodes_to_remove)