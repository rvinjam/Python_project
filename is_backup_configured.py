import requests
import read_jenkins_config
def verify_jenkins_backup_config(jenkins_url, jenkins_username, jenkins_password, backup_directory):
    try:
        # Make an HTTP request to Jenkins API to check backup directory
        api_url = f"{jenkins_url.rstrip('/')}/job/{backup_directory}/api/json"
        response = requests.get(api_url, auth=(jenkins_username, jenkins_password))

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            data = response.json()
            if 'builds' not in data:
                print(f"Error: Backup job '{backup_directory}' not found.")
                return False

            # Check for specific backup artifacts
            required_artifacts = ['config.xml', 'jobs', 'users']
            for artifact in required_artifacts:
                artifact_url = f"{jenkins_url.rstrip('/')}/job/{backup_directory}/lastSuccessfulBuild/artifact/{artifact}"
                response = requests.head(artifact_url, auth=(jenkins_username, jenkins_password))
                if response.status_code != 200:
                    print(f"Error: {artifact} not found in the backup directory.")
                    return False

            print("Jenkins backup configuration is valid.")
            return True

        else:
            print(f"Failed to retrieve Jenkins backup job. HTTP Status Code: {response.status_code}")
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False

# read jenkins config
jenkins_url, username, password = read_jenkins_config.read_jenkins_config()
backup_directory = ""

# Call the function to verify Jenkins backup configuration using REST API
verify_jenkins_backup_config(jenkins_url, username, password, backup_directory)