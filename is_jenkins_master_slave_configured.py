from jenkinsapi.jenkins import Jenkins
def get_master_node(jenkins_url):
    """Gets the master node of Jenkins."""
    server = Jenkins(jenkins_url)
    return server.get_nodes()[0]

def get_slave_nodes(jenkins_url):
    """Gets the slave nodes of Jenkins."""
    server = Jenkins(jenkins_url)
    return server.get_nodes()[1:]

def main():
    """Gets the master and slave nodes of Jenkins and prints them to the console."""
    jenkins_url = "http://localhost:8080"
    master_node = get_master_node(jenkins_url)
    slave_nodes = get_slave_nodes(jenkins_url)

    print("Master node:")
    print(master_node.name)

    print("Slave nodes:")
    for slave_node in slave_nodes:
        print(slave_node.name)

if __name__ == "__main__":
    main()