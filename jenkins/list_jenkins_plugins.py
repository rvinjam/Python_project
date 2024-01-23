import requests
import read_jenkins_config
def list_jenkins_plugins(jenkins_url, username, password):
   try:
       api_url = f"{jenkins_url.rstrip('/')}/pluginManager/api/json?depth=1"
       response = requests.get(api_url, auth=(username, password))
       if response.status_code == 200:
           data = response.json()
           plugins = data.get('plugins', [])
           if plugins:
               print("Installed Jenkins Plugins:")
               for plugin in plugins:
                   print(f"- {plugin['shortName']} ({plugin['version']})")
           else:
               print("No plugins found.")
       else:
           print(f"Failed to retrieve plugin information. HTTP Status Code: {response.status_code}")
   except Exception as e:
       print(f"Error: {e}")
# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
# Call the function to list Jenkins plugins
list_jenkins_plugins(jenkins_url, username, password)