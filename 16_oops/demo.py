# OOP - Object Oriented Programming

# class -> Blue Print 
# Student -> Real World Entity 

class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies():
        print("Student Info - Student Studies")
        
    # Statements 
    print("Student Information System")
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
        
# Object Creation
student_object = Student()    
# student_studies()
# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        
    # Statements 
    print("Student Information System")
    print("Student Name: "+student_name)
    print("Student Email: "+student_email)
        
# Object Creation
student_object = Student()    
# student_studies()
student_object.student_studies()

# Referring with objects 
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        print("Student Name: "+student_object.student_name)
        print("Student Email: "+self.student_email) # recommended 
        
        
# Object Creation
student_object = Student()    
# student_studies()
student_object.student_studies()

# Referring with objects 
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name)
        print("Student Email: "+self.student_email) # recommended 
        
        
# Object Creation
student_object = Student()    
# student_studies()
student_object.student_studies()

print("=" * 50)

# Working with multiple objects without Constructors 
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name)
        print("Student Email: "+self.student_email) # recommended  
        
# Object Creation
student_ravi = Student()    
student_ravi.student_studies()

student_john = Student()    
student_john.student_studies()

student_mike = Student()    
student_mike.student_studies()

print("=" * 50)

# Working with multiple objects with Constructors 
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    def student_studies(self):
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name)
        print("Student Email: "+self.student_email) # recommended  
        
# Object Creation
# student_ravi = Student()  # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'  
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@outlook.com")    
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com")    
student_mike.student_studies()

print("=" * 50)

# Instance Members 
class Student:
    # Has Something - Characteristics / Properties / Attributes / VARIABLES
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # Below are instance variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    # Below is Instance Method 
    def student_studies(self):
        print("Student Info - Student Studies")
        print("Student Name: "+self.student_name)
        print("Student Email: "+self.student_email) # recommended  
        
# Object Creation
# student_ravi = Student()  # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'  
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@outlook.com")    
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com")    
student_mike.student_studies()

print("=" * 50)


# Class Members 
class Student:
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Digital Edify"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # Below are instance variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    # Below is Instance Method 
    def student_studies(self):
        print("Student Info - Student Studies")
        print("From Institute: "+self.institute_name) # not recommended
        print("Student Name: "+self.student_name)
        print("Student Email: "+self.student_email) # recommended  
        
    # Class Method
    @classmethod 
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
    
        
# Object Creation
# student_ravi = Student()  # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'  
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@outlook.com")    
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com")    
student_mike.student_studies()

print("=" * 50)


# Class Members 
class Student:
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Digital Edify"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # Below are instance variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    # Below is Instance Method 
    def student_studies(self):
        print("Student Info - Student Studies")
        print("From Institute: "+Student.institute_name) # recommended
        print("Student Name: "+self.student_name)
        print("Student Email: "+self.student_email) # recommended  
        
    # Class Method
    @classmethod 
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # print(self.student_name) # Accessing instance data inside a class method gives error 
    
        
# Object Creation
# student_ravi = Student()  # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'  
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@outlook.com")    
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com")    
student_mike.student_studies()

# Class Method Calling /Accessing
Student.change_institute_name("Digital Lync") # recommended  
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@outlook.com")    
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com")    
student_mike.student_studies()

print("=" * 50)

# Static Members 
class Student:
    
    # Class Variable - "shared by all the objects" of the class 
    institute_name = "Digital Edify"
    
    # Constructor - initialize a newly created object's attributes
    def __init__(self,student_name,student_email):
        # Below are instance variables -> self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Does Something - Behaviors / Actions / Functions / METHODS
    # Below is Instance Method 
    def student_studies(self):
        print("Student Info - Student Studies")
        print("From Institute: "+Student.institute_name) # recommended
        print("Student Name: "+self.student_name)
        print("Student Email: "+self.student_email) # recommended  
        
    # Class Method
    @classmethod 
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        # print(self.student_name) # Accessing instance data inside a class method gives error 
    
    @staticmethod
    def something():
        return "I Do Something That Doesn't Associate with Class or Object"
    
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email # T & T 
    
        
# Object Creation
# student_ravi = Student()  # TypeError: Student.__init__() missing 2 required positional arguments: 'student_name' and 'student_email'  
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@outlook.com")    
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com")    
student_mike.student_studies()

# Class Method Calling /Accessing
Student.change_institute_name("Digital Lync") # recommended  
student_ravi = Student("ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("john","john@outlook.com")    
student_john.student_studies()

student_mike = Student("mike","mike@gmail.com")    
student_mike.student_studies()

# Call Static Method
print(Student.something())

print(Student.validate_email("ravi"))
print(Student.validate_email("ravi@gmailcom"))
print(Student.validate_email("ravi@gmail.com"))
print("=" * 50)