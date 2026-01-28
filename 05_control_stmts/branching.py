# Branching Structures / Statements (Jump Statements)

for num in range(1,11):
    print(num)

# break - help you exit the loops 
for num in range(1,11):
    if num == 5:
        break # stops the loop from here 
    print(num)
    
# continue - help you skip the current iteration 
for num in range(1,11):
    if num == 5:
        continue # skip the current iteration 
    print(num)

# pass - acts as a placeholder, does nothing
# Requirement - To Perform Some Future Operations 
# When Salary is above 25000 we want to do something 
emp_salary = 15000
if emp_salary > 25000:
    pass # ________   

# After 6 Months
emp_salary = 28000
if emp_salary > 25000:
    print("Promoted To Senior")
  
# Some other operations to work on
print("Working With Next Coming Scenario")

class Employee:
    pass 

class Manager:
    pass 