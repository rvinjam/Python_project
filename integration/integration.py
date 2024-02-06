# integration maturity score
#     - Check the deployment process (Manual or CI CD tools(devops pipelines- Jenkins, AWS DevOps, Azure DevOps etc.))
#     
#
#
#
import cicdtools_check
# Define criteria for maturity levels
criteria = {
    "CICD tools": 1,
   
}
 
# Initialize maturity score
maturity_score = 0
# Evaluate each criterion
for criterion, weight in criteria.items():
    while True:
        try:
            score1 = cicdtools_check.check_version_control()
            score2 = cicdtools_check.check_ci_pipeline()
            rating = score1 + score2
            
            if 1 <= rating <= 4:
                break
            else:
                print("Invalid rating.")
        except ValueError:
            print("Invalid Data.")
 
    maturity_score += weight * rating
             
# Output the maturity level based on the total score
if maturity_score >= 3:
    print("Integration maturity Level: Elite")
elif maturity_score >= 2:
    print("Integration maturity Level: High")
elif maturity_score >= 1:
    print("Integration maturity Level: Medium")
else:
    print("Integration maturity Level: Low")