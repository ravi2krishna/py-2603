# Exception Handling

# When No Errors -> Nothing To Handle 
print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = 5
print("Result: ", num1/num2)

print("Program Execution Completed")

# print("=" * 50)

# print("Program Execution Started")

# num1 = 10
# num2 = "five"
# print("Result: ", num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'

# print("Program Execution Completed")

# When Error -> Handle Exceptions using try & except 
print("=" * 50)

print("Program Execution Started")

num1 = 10
num2 = "five"
try:
    print("Result: ", num1/num2)
except:
    print("Don't divide numerics with text, this is maths")
print("Program Execution Completed")

# When Error -> Handle Exceptions using try & except 
print("=" * 50)

# print("Program Execution Started")

# num1 = 10
# num2 = 0
# print("Result: ", num1/num2) # ZeroDivisionError: division by zero

print("Program Execution Completed")

print("=" * 50)
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print("Result: ", num1/num2)
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")
print("=" * 50)

# When we come across multiple errors 

print("=" * 50)
print("Program Execution Started")
# data = [1,2,'python',0,5]
# data = [1,2,0,5]
data = [1,2,5]

for num in data:
    print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
print("Program Execution Completed")    
print("=" * 50)

# Common Message Scenario
print("=" * 50)
print("Program Execution Started")
data = [1,2,'python',0,5]

for num in data:
    try:
        print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except:
        print("OOPS! Something Went Wrong")
print("Program Execution Completed")    
print("=" * 50)


# Specific Exception Message 
print("=" * 50)
print("Program Execution Started")
data = [1,2,'python',0,5]

for num in data:
    try:
        print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    except TypeError:
        print("OOPS! Dividing String With Numbers is not supported")
    except ZeroDivisionError:
        print("OOPS! You Cannot Divide Number By Zero")
        print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")    
print("=" * 50)

# When there is error with else block
print("=" * 50)
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print("Result: ", num1/num2)
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful")
print("Program Execution Completed")
print("=" * 50)

# When there is no error with else block
print("=" * 50)
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print("Result: ", num1/num2) # Verify Login Credentials
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful") # Then Only Check OTP
print("Program Execution Completed")
print("=" * 50)


# finally -> run this code for sure 
print("=" * 50)
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print("Result: ", num1/num2)
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful")
finally:    
    print("Closing All Opened Streams Like Files & Databases Connections")
    print("Program Execution Completed")
print("=" * 50)

# Create Custom exceptions
class MyCustomError(Exception):
    pass 

# Voting App 
age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")
    
# Custom Age Exception    
class AgeError(Exception):
    pass 

# Voting App With Custom Age Exception    
# age = int(input("Enter Age: "))
# if age < 18:
#     raise AgeError
# else:
#     print("You Can Vote")
    
# Voting App With Custom Age Exception with Message 
# age = int(input("Enter Age: "))
# if age < 18:
#     raise AgeError("Your Age Must Be at least 18 Years To Vote")
# else:
#     print("You Can Vote")
    
# Handle Age Exception 
age = int(input("Enter Age: "))
try:
    if age < 18:
        raise AgeError("Your Age Must Be at least 18 Years To Vote")
except AgeError:
    print("You are not 18 Yet")
else:
    print("You Can Vote")
    
# ID Error 
class IDError(Exception):
    pass

# Custom ID Exception 
class IDError(Exception):
    pass 

# age = int(input("Enter Age: "))
# if age < 18:
#     raise AgeError("Your Age Must be at least 18 years to vote")
# else:
#     has_id = input("Do You Have ID? (yes/no) ")
#     if has_id != "yes":
#         raise IDError("You Must Have ID To Enter")
# print("You Can Vote")

# Handle Above Exceptions Now 
age = int(input("Enter Age: "))
try:
    if age < 18:
        raise AgeError("Your Age Must be at least 18 years to vote")
    else:
        has_id = input("Do You Have ID? (yes/no) ")
        if has_id != "yes":
            raise IDError("You Must Have ID To Enter")
except AgeError:
    print("You are not 18 Yet")
except IDError:
    print("Carrying ID is mandatory")
else:
    print("You Can Vote")