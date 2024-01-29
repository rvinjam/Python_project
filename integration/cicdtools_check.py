import os
import subprocess
import pipeline_stages_count

def check_version_control():
    if os.path.isdir(".git"):
        #print("Version Control: Git repository found.")
        return 1
    else:
        #print("Version Control: No Git repository found.")
        return 0

def check_ci_pipeline():
    ci_config_files = ["Jenkinsfile", ".travis.yml",
                       ".gitlab-ci.yml", "azure-pipelines.yml" , "buildspec.yml", "appspec.yml"]
    for config_file in ci_config_files:
        if os.path.isfile(config_file):
            return 1
        
        else:
            # Check for GitHub Actions workflow files
            if  os.path.isdir('.github/workflows'):
             github_actions_files = [f for f in os.listdir('.github/workflows') if f.endswith('.yml')]
             if github_actions_files:
                return 1
        return 0
def check_automated_tests():
    # You might use a specific testing framework like pytest or unittest here
    # Check for the existence of automated tests or test directories
    if os.path.isdir("tests") or "test_" in os.listdir():
        print("Automated Tests: Automated tests found.")
    else:
        print("Automated Tests: No automated tests found.")

def check_deployment_automation():
    # Example: Check if deployment scripts exist
    if os.path.isfile("deploy.sh"):
        print("Deployment Automation: Deployment script found.")
    else:
        print("Deployment Automation: No deployment script found.")
# Add more functions for other checks (e.g., infrastructure as code, monitoring)
def check_more_stages():
        file_path = "C:/Users/ramarao.vinjam/OneDrive - HCL Technologies Ltd/Ramarao/HCL-03-08-2021/Python_project/integration/Jenkinsfile"
        target_word = "stage"
        word_count = pipeline_stages_count.count_word_in_file(file_path, target_word)
        print(f"The word '{target_word}' appears {word_count} times in the file.")
        if word_count >=2:
         print("Pipeline has moret han two stages.")
         return 1
        else:
         print("Pipeline has lessthan or equal to  two stages..")
         return 0
def has_code_quality_stage():
    # Example: Check if deployment scripts exist
    if os.path.isfile("deploy.sh"):
        print("Deployment Automation: Deployment script found.")
    else:
        print("Deployment Automation: No deployment script found.")
if __name__ == "__main__":
    print("CI/CD Maturity Check Script\n")
    check_version_control()
    check_ci_pipeline()
    check_automated_tests()
    check_deployment_automation()
    check_more_stages()
    # Add more function calls for additional checks

    print("\nMaturity checks completed.")
