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

num1 = 10
num2 = 0
try:
    print("Result: ", num1/num2)
except:
    print("OOPS! We Got an Error - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")