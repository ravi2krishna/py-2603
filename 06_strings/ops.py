# String Methods / Operations 

# text = "python"
# print(dir(text))

# Simulate Gmail Functionality 
# RaVI2KRIshNA -> ravi2krishna@gmail.com 
email = input("Enter Email ID: ")
print("Original Email: "+email)
# Transform to lower case
format_email = email.lower()
print("Transformed Email: "+format_email)
# Update @gmail.com 
format_email = format_email + "@gmail.com"
print("Transformed Email: "+format_email)

#                RaVI2KRIshNA
# Remove Spaces 
format_email = format_email.strip()
print("Transformed Email: "+format_email)

# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm

pan = input("Enter PAN ID: ")
print("Original PAN: "+pan) # $ampui9916s
print(pan.isalnum())

if pan.isalnum() and len(pan) == 10:
    print("Original PAN: "+pan)
    print("Formatted PAN: "+pan.upper())
else:
    print(f"PAN {pan} is Invalid")
    
# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
# https://www.businessbloomer.com/wp-content/uploads/2014/11/woocommerce-add-coupon-automatically-to-cart-if-product.png

mobile = input("Enter Phone Number With ISD Code: ")
print(mobile.startswith("+91"))

if mobile.startswith("+91"):
    print("Calling India Number - Chared in Rupees")
elif mobile.startswith("+33"):
    print("Calling France Number - Chared in Euros")
elif mobile.startswith("+1"):
    print("Calling US Number - Chared in Dollars")
else:
    print("Invalid Number Calling US, INDIA & France Only Supported")
    
# Simulate Email Synchronization 
source_email = input("Enter Source Email ID: ")
# print(source_email.endswith("@gmail.com"))
destination_email = input("Enter Destination Email ID To Backup: ")

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Backup Process Started")
else:
    print("Email Backup Process Failed - Source & Destination Didn't Match")


# Simulate Data Operations Work: CSV Data from a file and perform some operations 
# Name,Email,Age,City,Job_Role
# emp_data = "Johnny,john@apple.com,45,Hyd,Developer"
# emp_data = "Ravi,john@apple.com,45,Hyd,Developer"
emp_data = "Ravi,john@apple.com,45,Hyd,Admin"
# Requirement: Display Employee Name & Job Role 
emp_name = emp_data[0]
print("Employee Name: ",emp_name)

emp_name = emp_data[0:6]
print("Employee Name: ",emp_name)

# Using Above we are hard coding logic which is not good 

emp_data = "Ravi john@apple.com 45 Hyd Admin"
emp_data = "Johnny john@apple.com 45 Hyd Admin"
emp_data_extraction = emp_data.split()
print(emp_data_extraction)
print("Employee Name: ",emp_data_extraction[0])

emp_data = "Ravi,john@apple.com,45,Hyd,Admin"
emp_data = "Mark,john@apple.com,45,Hyd,Developer"
emp_data_extraction = emp_data.split(",")
print("Employee Name: ",emp_data_extraction[0])
print("Employee Role: ",emp_data_extraction[-1])

# Simulate Amazon Order Email Confirmation Template Based System
order_template = "Hello your order with order_id has been shipped"
order_ids = "AMZ-123,AMZ-234,AMZ-345,AMZ-456,AMZ-567"
orders_extraction = order_ids.split(",")
for amazon_order_id in orders_extraction:
    send_email = order_template.replace("order_id",amazon_order_id)
    print(send_email)