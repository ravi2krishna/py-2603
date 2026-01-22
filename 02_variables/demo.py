# Variables 

# Assign Data (Store Data)
student_name = "Ravi" # String
student_age = 25 # int
student_gpa = 9.5 # float
student_passed = True # now student is passed  # boolean 
student_aadhar = None # Absence of value # NoneType 

# Retrieve Data (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(student_aadhar)

# Retrieve Data (Get Data)
print("======= Student Info ========")
# print("Student Name is "student_name) # SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Student Name is " + student_name)
# print("Student Name is " , student_name) 
# print("Student Age is " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age is ", student_age)
print("Student GPA is ", student_gpa)
print("Student Passed ", student_passed)
print("Student Aadhar ID ", student_aadhar)

# type(): used to tell data type 
type(student_name)
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(student_aadhar))

# id(): used to get memory address
print(id(student_name))
print(id(student_age))
print(id(student_gpa))

# Memory Model In Python 
value_x = 10 
print(id(value_x)) # 4374159656

value_y = 20 
print(id(value_y)) # 4374159976

value_z = 10 
print(id(value_z)) # 4374159656

# Complex Data Type 
list_of_number_x = [1,2,3,4]
list_of_number_y = [5,6.7]
list_of_number_z = [1,2,3,4]
print(list_of_number_x)
print(list_of_number_x[0])
print(list_of_number_x[1])
print(id(list_of_number_x))
print(id(list_of_number_y))
print(id(list_of_number_z))
print(id(list_of_number_x[0]))
print(id(list_of_number_x[1]))
print(id(list_of_number_z[0]))


