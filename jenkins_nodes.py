from jenkinsapi.jenkins import Jenkins

# Define the Jenkins URL
jenkins_url = "http://localhost:8080"

# Create a Jenkins server object
jenkins_server = Jenkins(jenkins_url)


# Get the list of all nodes
nodes = jenkins_server.get_nodes()

# Print the list of all nodes
for node in nodes:
    print(node.name)

# Get the list of all master nodes
master_nodes = jenkins_server.get_master_nodes()

# Print the list of all master nodes
for master_node in master_nodes:
    print(master_node.name)

# Get the list of all slave nodes
slave_nodes = jenkins_server.get_slave_nodes()

# Print the list of all slave nodes
for slave_node in slave_nodes:
    print(slave_node.name)