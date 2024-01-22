from github import Github
# Replace 'your_access_token' with your GitHub access token
access_token = 'your_access_token'
# Create a GitHub instance using the access token
github_instance = Github(access_token)
# Specify the repository details
repo_owner = 'owner_username'
repo_name = 'repository_name'
# Get the repository
repository = github_instance.get_repo(f'{repo_owner}/{repo_name}')