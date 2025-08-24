



# This block of code allows setting the number of failed attempts allowed
# before the program exits. The default is set to 3 attempts. Yes, that includes 
defaultAttempts = 3
def setFailedAttempts(attempts):
    global defaultAttempts
    defaultAttempts = attempts
    

def login():
    user_name = "admin"
    pwd = "admin1"

    for failed_attempts in range(defaultAttempts,0,-1):
        user_name_input = input("Input Username: ")
        pwd_input = input("Input Password: ")
        if user_name_input == user_name and pwd_input == pwd:
            print("Login successful")
            break
            
        else:
            print(f"Login failed. You have {failed_attempts} attempts left.")

# login() 
# Issued solved the 2 times login issue. in the first attempt.
# The issue was due to calling login() function twice in main.py

