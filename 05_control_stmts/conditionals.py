# Conditionals 

# Indentation

print("Hello")
print("Python")
# print("Hello") # IndentationError: unexpected indent


# if condition - Incorrect Indentation
# if True:
# print("Python") # IndentationError: expected an indented block after 'if' statement on line 11

# if condition - Correct Indentation
if True:
 print("Python")
 print("Block") 
 print("Of") 
 print("Code") 
#  print("Check") # IndentationError: unexpected indent
 
# if condition - Correct Indentation
if True:
  print("Python")
  print("Block") 
  print("Of") 
  print("Code") 
  print("Check")
  
# if condition - Correct Indentation
if True:
    print("Python")
    print("Block") 
    print("Of") 
    print("Code") 
    print("Check")
    
# if condition
if 5 > 2:
    print("yes 5 > 2 that is correct")
    
if 5 < 2:
    print("yes 5 < 2 that is correct")

num = -10
if num > 0:
    print("given num is positive")
if num < 0:
 print("given num is negative")
 

# if else condition
num = 10
if num > 0:
    print("given num is positive")
else:
    print("given num is negative")
    
# if else condition using input()
# name = "Ravi"
name = input("What Is Your Name: ")
print(name)
print("Welcome "+name)
print("Welcome name")
print(f"Welcome {name}") 

# if else condition dynamic
num = input("Enter Number: ")
num = int(num) # Type Casting
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"given {num} is positive")
else:
    print(f"given {num} is negative")
    
# if else condition dynamic
num = int(input("Enter Number: ")) # Type Casting
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"given {num} is positive")
else:
    print(f"given {num} is negative")
    
# Voting App 
age = int(input("Enter Your Age: "))  
if age >= 18:
    print("You Can Vote")
else:
    print(f"You Cannot Vote as you are still {age}")

# "conditional expression"
age = int(input("Enter Your Age: "))  
status = "You Can Vote" if age >= 18 else "You Cannot Vote"
print(status)

# elif ladder 
# Check For Grades 
marks = int(input('Enter Marks: '))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 50:
    print("D Grade")
elif marks >= 35:
    print("E Grade")
else:
    print("FAIL")
    
# match/case - 1
error_code = int(input("What Code Did You See: "))
match error_code:
    case 403:
        print("Forbidden Error")
    case 404:
        print("Not Found Error")
    case 200:
        print("Success - OK")
    case 502:
        print("Internal Server Error")
    case _:
        print("Invalid Error Code")
        
# match/case - 2
user_role = input("Enter Your Role: ")
match user_role:
    case "lead" | "manager":
        print("You Have List, Read & Write Access") 
    case "developer" | "tester":
        print("You Have List & Read Access") 
    case "guest":
        print("You Have List Access")
    case _:
        print("Access Denied")
        
