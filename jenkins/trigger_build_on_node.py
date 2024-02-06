import requests
import read_jenkins_config
def trigger_build_on_node(jenkins_url, job_name, node_name, username, password):
   try:
       # REST API URL for triggering a build
       api_url = f"{jenkins_url.rstrip('/')}/job/{job_name}/build"
       # Additional parameters to specify the node where the build should run
       params = {
           'NODE_NAME': node_name
       }
       # Make the REST API request to trigger the build
       response = requests.post(api_url, params=params, auth=(username, password))
       if response.status_code == 201:
           print(f"Build triggered successfully on node '{node_name}' for job '{job_name}'.")
       else:
           print(f"Failed to trigger build. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
job_name = ""
node_name = ""
# Call the function to trigger a build on a specific node
trigger_build_on_node(jenkins_url, job_name, node_name, username, password)