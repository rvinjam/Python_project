# Define criteria for maturity levels
criteria = {
    "PolicyAutomation": 3,
    "ComplianceManagement": 3,
    "RiskManagement": 3,
    "ProcessDocumentation": 2,
    "AutomationAndTooling": 3,
    "MonitoringAndMetrics": 2,
    "CollaborationAndCommunication": 2,
    "ContinuousFeedback": 2,
    "ContinuousImprovement": 3,
    "SecurityIntegration": 3,
}
 
# Initialize maturity score
maturity_score = 0
 
# Evaluate each criterion
print("On a scale of 1 to 3, how well does your DevOps maturity meet")
for criterion, weight in criteria.items():
    while True:
        try:
            rating = int(input(f" {criterion}? "))
            if 1 <= rating <= 3:
                break
            else:
                print("Invalid rating. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
 
    maturity_score += weight * rating
 
# Output the maturity level based on the total score
if maturity_score > 24:
    print("Maturity Level: Elite")
elif maturity_score == 24:
    print("Maturity Level: High")
elif maturity_score >= 16:
    print("Maturity Level: Medium")
else:
    print("Maturity Level: Low")