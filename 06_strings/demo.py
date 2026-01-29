# Strings In Python 

# Single Line Strings
s1 = 'hello'
print(s1)

s2 = "hello"
print(s2)

s3 = """hello""" # not recommended for single line strings 
print(s3)

s4 = '''hello''' # not recommended for single line strings 
print(s4)

# Multi Line Strings
# define_python = 'Python is a high-level, general-purpose programming language. 
#         Its design philosophy emphasizes code readability with the 
#         use of significant indentation. '
# print(define_python) # SyntaxError: unterminated string literal (detected at line 17)

# Multi Line Strings
define_python = '''Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the 
        use of significant indentation. '''
print(define_python)

define_python = """Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the 
        use of significant indentation. """
print(define_python)

# Need single quote in a string 
question = "How Are You ?"
# answer = 'i'm fine' # SyntaxError: unterminated string literal (detected at line 35)
answer = "i'm fine"
print(answer)


# Need double quote in a string 
question = "How Are You ?"
# answer = "i"m fine"  # SyntaxError: unterminated string literal (detected at line 42)
answer = 'i"m fine'
print(answer)

# Need single & double quote in a string 
question = "How Are You ?"
answer = '''i"m fine i'm fine'''
answer = """i"m fine i'm fine"""
print(answer)

# Accessing Strings 
text = "python"
print(text)

# Accessing Characters In Strings Using Index
# Positive Index
print(text[0])
print(text[1])

# Negative Index
print(text[-1])
print(text[-2])

# Beyond Index Range
# print(text[10]) # IndexError: string index out of range

# Access All Characters
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# Access All Characters
text = "python"
for char in text:
    print(char)
    
# len(): used to check length of string
print("Length Of String: ", len(text))

# Slicing -> string[start:end:step]
text = "python"
# print(text[]) # SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(text[::])
print(text[0:3:1]) # p y t
print(text[0:3]) # p y t
print(text[1:3]) # y t
print(text[0:5:2]) # p t o

text = "python"
        #     0 1 2 3 4    5
        #     p y t h o    n 
        #    -6 -5 -4 -3 -2 -1

print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # tho / tno -> empty 
print(text[-4:-6:-1])    # ty 

# String Concatenation 
g = "good"
m = "morning"
print(g+m)

# Formatted String Literals (f-strings)
age = 30
# print("My age is "+age) # TypeError: can only concatenate str (not "int") to str
print(f"My age is {age}")

# String Repetition 
laugh = "Haha"
print(laugh)

hard_laugh = "HahaHahaHahaHahaHaha"
print(hard_laugh)

hard_laugh = laugh * 10
print(hard_laugh)

# String Immutability -> cannot be changed/modified
greet = "hello" # Transform To Hello
print(greet)
print(greet[0])
# greet[0] = 'H' # TypeError: 'str' object does not support item assignment
print(greet)

# List Objects are Mutable In Nature -> can be changed/modified
greet = ['h','e','l','l','o']
print(greet)
print(greet[0])
greet[0] = 'H'
print(greet)
