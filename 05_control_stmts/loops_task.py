# Simulate ATM Pin Functionality (ATM/OTP/Passwords etc)

actual_otp = 2345

# print(len(actual_otp)) # TypeError: object of type 'int' has no len()
# actual_otp = "234578"
# print(len(actual_otp))

attempts = 3

while attempts > 0:
    print(f"You Have {attempts} Attempts Left")
    user_otp = int(input("Enter OTP: "))
    
    if (len(str(user_otp))) != 4:
        print("Transaction Failed - OTP Must be 4 Digits")
        attempts -= 1
        continue 
    
    if user_otp == actual_otp:
        print("Transaction Success")
        break 
    else:
        print("Transaction Failed - Incorrect OTP")
        attempts -= 1
        
else:
    print("Maximum Attempts Reached, Try after 24 Hours ")
    