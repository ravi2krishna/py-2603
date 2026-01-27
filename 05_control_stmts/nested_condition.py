# Nested Conditionals 
# where the inner condition is only checked if the outer condition is true. 

if True:
    print("1")
    if True:
        print("2")
        
if False:
    print("3")
    if True:
        print("4")
        
# Nested Use case
age = int(input("Enter Your Age: "))
if age >= 18:
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID")
else:
    print("You Cannot Vote - Under Age")
