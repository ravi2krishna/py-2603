# Operators 

# Arithmetic Operators
num1 = 10 
num2 = 5 

print("Sum Of Numbers: ", num1+num2)
print("Difference Of Numbers: ", num1-num2)
print("Product Of Numbers: ", num1*num2)
print("Division Of Numbers: ", num1/num2)
print("Modulus Of Numbers: ", num1%num2)

print("Floor Division Of Numbers: ", num1//num2)
print("Normal Division Of Numbers: ", 3/2)
print("Floor Division Of Numbers: ", 3//2)

print("Exponentiation Of Numbers: ", 3 ** 2) # 3 ^ 2

# Calculate EMI for Car Purchase
# https://www.cardekho.com/carmodels/Tata/Tata_Sierra
# https://media.geeksforgeeks.org/wp-content/uploads/20240131135654/emi-formula-copy2.webp

# Compound Assignment Operators
num = 10
num = num + 5 # long format 
print(num)

num = 10
num += 5 # short format 
print(num)

num = 10
num *= 5 # short format 
print(num)

# Increment - increase a value, used in loops in future sessions 
count = 1
# count++ # SyntaxError: invalid syntax
count += 1
print(count)

# Decrement - decrease a value, used in loops in future sessions 
count = 10
# count-- # SyntaxError: invalid syntax
count -= 1
print(count)

# Comparison Operators
num1 = 3
num2 = 2
num3 = 3
print(num1 == num2)
print(num1 == num3)
print(num1 != num2)
print(num1 > num2)

print("===============")

# Logical Operators
num1 = 4
num2 = 3
num3 = 2
num4 = 1

print(num1 > num2 and num3 > num4) # T and T -> T
print(num1 < num2 and num3 > num4) # F and T -> F

print(num1 < num2 or num3 > num4) # F or T -> T

print(num1 < num2) # F
print(not num1 < num2) # T

print("===============")

# Membership Operators
data = "python is interpreted language"
find_word = "python"
find_word = "java"
status = find_word in data
print(status)

employee_ids = ["101","102","103","110"]
find_emp_id = "105"
find_emp_id = "102"
status = find_emp_id in employee_ids
print("Employee Found: ", status)

employee_ids = ["101","102","103","110"]
find_emp_id = "105"
status = find_emp_id not in employee_ids
print("Employee Not Found: ", status)

# NOTE: 
data = 123456789
find_one = 1
# status = find_one in data # TypeError: argument of type 'int' is not iterable
print(status)

# string -> data = "python is interpreted language"
data = "python is interpreted language"
print(dir(data))
print(data.upper())

# employee_ids = ["101","102","103","110"] -> list data
employee_ids = ["101","102","103","110"]
print(type(employee_ids))
print(dir(employee_ids))

# data = 123456789 -> int
data = 123456789
print(type(data))
print(dir(data))

# Identity Operators
n1 = 10
n2 = 10 
print(id(n1))
print(id(n2))
print(n1 is n2)
print(n1 == n2)

n1 = [1,2]
n2 = [1,2]
print(n1 == n2)
print(n1 is n2) 
print(id(n1))
print(id(n2))

# Bitwise Operators
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000001 -> 1
print(n1 & n2)
print(5 & 3) 

n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000111
print(n1 | n2)