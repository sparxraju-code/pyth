def check_password_strength(password):
    Chk = 0
    if len(password) <= 7:
        print ("Password is too short. It must be at least 8 characters")     
        Chk = 1   
    if not any(ch.isupper() for ch in password):
        print ("Password must contain at least one uppercase letter")
        Chk = 1
    if not any(ch.islower() for ch in password):
        print ("Password must contain at least one lowercase letter")
        Chk = 1
    if not any(ch.isdigit() for ch in password):
        print ("Password must contain at least one number")
        Chk = 1
    special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|"
    if not any(ch in special_chars for ch in password):
        print ("Password must contain at least one special character")
        Chk = 1
    
    if Chk == 0: 
        return True
    else:
        return False 

password = input("Enter your password: ")
Result = check_password_strength(password)

if Result == True:
    print ("Password is valid.")
else:
    print("Please retry with a stronger password.")