from github import Github
access_token = ''
# Create a GitHub instance using the access token
github_instance = Github(access_token)
# Specify the repository details
repo_owner = ''
repo_name = ''
# Get the repository
repository = github_instance.get_repo(f'{repo_owner}/{repo_name}')