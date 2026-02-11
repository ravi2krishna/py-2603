# Functional Style Programming 

# Without Functions 

num1 = 10
num2 = 5

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)

# Another user wants to calculate with 20 & 5 
num1 = 20
num2 = 5

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)

# Another user wants to calculate with 200 & 50
num1 = 200
num2 = 50

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 20)

# With Functions 
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# User 1 -> 10 & 5
num1 = 10
num2 = 5
math_ops()
print("=" * 20)
# User 2 -> 20 & 5
num1 = 20
num2 = 5
math_ops()
print("=" * 20)
# User 3 -> 200 & 50
num1 = 200
num2 = 50
math_ops()
print("=" * 20)

# Why not this
# math_ops(200,100) # TypeError: math_ops() takes 0 positional arguments but 2 were given
print("=" * 20)

# With Functions & parameters
def math_ops(num1,num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'n1' and 'n2'
math_ops(10,5)
print("=" * 20)
math_ops(20,5)
print("=" * 20)
math_ops(200,50)
print("=" * 20)
# math_ops(200) # TypeError: math_ops() missing 1 required positional argument: 'num2'
print("=" * 20)

# simulate ecommerce application total_cart
def amazon_user_ravi_cart(p1,p2,p3):
    # 200 lines of code to add products to cart 
    print(p1 + p2 + p3)
    
def amazon_user_mike_cart(p1,p2,p3):
    # 200 lines of code to add products to cart 
    print(p1 + p2 + p3)
    
def amazon_user_john_cart(p1,p2,p3):
    # 200 lines of code to add products to cart 
    print(p1 + p2 + p3)
    
# Amazon cart 
def amazon_users_cart(user_id,products_list):
    print(user_id + " - " +products_list)
    
    
# Positional Arguments
def math_ops(num1,num2):
    print(num1 + num2)
    
math_ops(2,3)
math_ops(3,2)

print("=" * 20)

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
    
employee_info("hyderabad","ravi","ravi@gmail.com")
employee_info("ravi","ravi@gmail.com","hyderabad")

print("=" * 20)

# Keywords Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info("hyderabad","ravi","ravi@gmail.com")    
employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")

print("=" * 20)

# No Default Arguments 
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at {emp_location}")

employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com",org_name="Google")
employee_info(emp_location="pune",emp_name="krishna",emp_email="krishna@gmail.com",org_name="Google")
# 200th employee    
employee_info(emp_location="delhi",emp_name="ram",emp_email="ram@gmail.com",org_name="Google")
    
print("=" * 20)    
    
# Default Arguments -> Always Org Name is Google i.e Default Argument
def employee_info(emp_name,emp_email,emp_location,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at {emp_location}")

employee_info(emp_location="hyderabad",emp_name="ravi",emp_email="ravi@gmail.com")
employee_info(emp_location="pune",emp_name="krishna",emp_email="krishna@gmail.com")
# 200th employee    
employee_info(emp_location="delhi",emp_name="ram",emp_email="ram@gmail.com")
employee_info(emp_location="new york",emp_name="mark",emp_email="mark@meta.com",org_name="Meta")

# Default Arguments Placement Requirement (Wrong Placement)
# def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile): # Non-default argument follows default argument
#     print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at {emp_location}")

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at {emp_location}")

def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile="999"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at {emp_location}")

print("=" * 20)   

# Arbitrary Positional Arguments

# def add_numbers(n1):

# def add_numbers(n1,n2):

# def add_numbers(n1,n2,n3):

# def add_numbers(n1,n2,n3,n10):

# def add_numbers(*nums):

def add_numbers(*nums):
    print(nums)
    
add_numbers(10)    
add_numbers(10,20)    
add_numbers(10,20,30,40,50)  # 

def add_numbers(*nums):
    total = 0
    for num in nums:
        total += num # total = total + num 
    print(f"Total Sum is {total}")

add_numbers(10,20)
add_numbers(10,20,30,40,50)
print("=" * 20) 
# Real World Use case: Carts In Ecommerce Applications 

# Arbitrary Keywords Arguments
def profile(**info):
    print(info)
    
profile(fname="Ravi")
profile(fname="Ravi",lname="Krishna",email="ravi2krishna@gmail.com")

print("=" * 20) 

# Real word use case -> jan=2000,feb=3500,mar=6000 -> Req: Total Transactions Value & Number Of Transactions
def bank_transactions(**transactions):
    print(transactions)
    total = 0
    transaction_count = 0
    for transaction in transactions:
        # print(transaction)
        # print(transactions[transaction])
        total += transactions[transaction]
        transaction_count += 1
    print(f"You have done {transaction_count} transactions which Totals To {total}")    
bank_transactions(jan=2000,feb=3500,mar=6000) 

print("=" * 20) 