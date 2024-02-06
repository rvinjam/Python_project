import os 
def is_running_in_docker():
     # Check if the '/.dockerenv' file 
     # exists, which is typically present 
     # in a Docker container 
     return os.path.exists('/.dockerenv') 
if is_running_in_docker(): 
    print("Jenkins is running in a Docker container.") 
else: print("Jenkins Server is not running in a Docker container.")