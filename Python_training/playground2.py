


user_name = "admin"
pwd = "admin1"


# def LoginFunc():
#     for failed_attempts in range(3,0,-1):
#         user_name_input = input("Input Username: ")
#         pwd_input = input("Input Password: ")
#         if user_name_input == user_name and pwd_input == pwd:
#             print("Login successful")
#             break
#         else:
#             print("Username or password is incorrect. ", failed_attempts, " attempts left.")


def setCredentials(maxFailedAttempts=3):
    for failed_attempts in range(maxFailedAttempts,0,-1):
        user_name_input = input("Input Username: ")
        pwd_input = input("Input Password: ")
        if user_name_input != user_name or pwd_input != pwd:
            print(f"Login failed. You have {failed_attempts-1} attempts left.")
        else:
            print("Login successful")
            break
        if failed_attempts == 1:
            print("No attempts left. Exiting program.")
            exit(0)
    
setCredentials(3)

