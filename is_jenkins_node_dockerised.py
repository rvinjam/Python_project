import requests
import read_jenkins_config
def is_node_dockerized(jenkins_url, node_name, username, password):
   try:
       # REST API URL for obtaining information about the node
       api_url = f"{jenkins_url.rstrip('/')}/computer/{node_name}/api/json"
       # Make the REST API request to get information about the node
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           data = response.json()
           # Check if the node is running as a Docker container
           is_dockerized = data.get('jnlpAgent', False)
           if is_dockerized:
               print(f"Node '{node_name}' is running as a Docker container.")
           else:
               print(f"Node '{node_name}' is not running as a Docker container.")
       else:
           print(f"Failed to retrieve node information. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")

# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
node_name = "your_node_name"
# Call the function to check if a specific node is Dockerized
is_node_dockerized(jenkins_url, node_name, username, password)