# Looping Structures / Statements (Iteration Statements)

# while loop 
# while True:
#     print("This Forms An Infinite Loop")
#     print("..")
#     print(".....")
    # To terminate the loop use control + c on keyboard
    
# while loop 
while False:
    print("This Forms An Infinite Loop")
    print("..")
    print(".....")
    
# Counters 
count = 1
while count <= 5:
    print("Count: ",count)
    count+=1
    
# You found a lost phone, trying to break passcode 
# At which attempt the phone will be unlocked ?

actual_passcode = "4532"
user_given_pin = ""

while user_given_pin != actual_passcode:
    user_given_pin = input("Enter PIN: ")
print("Phone Unlocked")

# for loop 
prices_products = [1000,1500,2500,5000] # [1000-500,1500-500,2500-500,5000-500]
# Some offer is running - discount of 500 on each product
print(prices_products[0]- 500)
print(prices_products[1]- 500)
print(prices_products[2]- 500)
print(prices_products[3]- 500)

# for loop -> now  have 1000 products
prices_products = [1000,1500,2500,5000,8000,1000,12000,15000] # [1000-500,1500-500,2500-500,5000-500]
# Some offer is running - discount of 500 on each product
for price in prices_products:
    print(price - 500)
    
# Say Hello
print("Hello")

# Now Say Hello 10 Times 
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# for with range()
for num in range(0,5,1):
    print(num)
    
for num in range(7,13,1):
    print(num)
    
for num in range(5):
    print(num)
    
for num in range(2,5):
    print(num)
    
for num in range(5,50,5):
    print(num)
    
for num in range(1,10,1):
    print(num)

for num in range(1,10,-1):
    print(num)
    
for num in range(10,1,-1):
    print(num)
    
# Now Say Hello 10 Times 
for num in range(10):
    print("Hello")
    
for num in range(1,-10,-1):
    print(num)