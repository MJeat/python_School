
user_name = "admin"
pwd = "admin1"
for failed_attempts in range(3,0,-1):
    user_name_input = input("Input Username: ")
    pwd_input = input("Input Password: ")
    if user_name_input == user_name and pwd_input == pwd:
        print("Login successful")
        break
    else:
        print("Username or password is incorrect. ", failed_attempts, " attempts left.")