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
