# Define criteria for maturity levels
criteria = {
    "Integration": 3,
    "Configuration": 3,
    "Security and Vulnerability": 3,
    "Reliability": 2,
    "Culture": 3,
    "Software Delivery Performance": 2,
    "Team performance": 2,
    "Organization performance": 2,
    "Operational performance": 3,
    
}
 
# Initialize maturity score
maturity_score = 0
 
# Evaluate each criterion
print("On a scale of 1 to 4, how well does your DevOps maturity meet")
for criterion, weight in criteria.items():
    while True:
        try:
            rating = int(input(f" {criterion}? "))
            if 1 <= rating <= 4:
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