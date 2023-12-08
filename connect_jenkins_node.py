import requests
def connect_node(jenkins_url, node_name, username, password):
   try:
       # REST API URL for connecting a node
       api_url = f"{jenkins_url.rstrip('/')}/computer/{node_name}/launchSlaveAgent"
       # Make the REST API request to connect the node
       response = requests.post(api_url, auth=(username, password))
       if response.status_code == 200:
           print(f"Node '{node_name}' connected successfully.")
       else:
           print(f"Failed to connect node. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# Replace these with your Jenkins server details and the specific node name
jenkins_url = "http://localhost:8080"
username = "ramarao"
password = "Jenkins@123"
node_name = "your_node_name"
# Call the function to connect a specific node
connect_node(jenkins_url, node_name, username, password)