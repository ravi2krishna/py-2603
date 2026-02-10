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