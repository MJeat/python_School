'''
Expected Output: [2025-02-18 14:33:00] [LOGIN] User: Alice, Status: Success, IP: 192.168.1.1

This program is a beginner cybersecurity logs detection and logs capture. This program has 3 functions: main, if_User_db_isEmpty(), and if_User_db_isNotEmpty()

1. Use if_User_db_isEmpty() if when the datebase is empty and you want to create a new credentials
2. Use if_User_db_isNotEmpty() if when the datebase is not empty and you want to log in and capture logs
3. main() is the caller of both functions

Additionally, there should be a logs.txt file where the captured logs are stored.

'''

from datetime import datetime
import socket

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
hostname = socket.gethostname() # This is your computer name
ipAddr = socket.gethostbyname(hostname) # This is your IPv4 of that computer

def main():
    # Use this if the database of the user and password are not known. You are trying to create new credentials.
    #if_User_db_isEmpty()

    # Use this if the database of the user and password are known. You are trying to look out for password or username brute force or multiple attempts.
    if_User_db_isNotEmpty()

def if_User_db_isEmpty():
    # User and Password database
    db = {}

    # For activity, puts login, file access, password failed attempts, and logout
    activity1= "" # Initializing
    status = ""
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        usr = input("Username: ")
        passwd = input("Password: ")
        

        if usr and passwd != "":
            activity1 = "LOGIN"
            status = "Success"
            db[usr] = passwd
            print(db)

            break
        else:
            print("Please Do Not Leave Blanks or Spaces")
    log_line1 = f"[{timestamp}] [{activity1}] User: {usr}, Status: {status}, IP: {ipAddr}"

    activity2 = ""
    while True:
        timestamp2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logout = input("Exit to Logout: ").lower()
        if logout == "exit":
            activity2 = "LOGOUT"
            break
        else:
            print("Type again, pal...")
    log_line2 = f"[{timestamp2}] [{activity2}] User: {usr}, Status: {status}, IP: {ipAddr}"


    print(log_line1)
    print(log_line2)

def if_User_db_isNotEmpty():
    while True:
        # User and Password database
        db = {"admin": "admin"}

        # Logging In
        while True:
            usr = input("Username: ").strip()
            passwd = input("Password: ").strip()

            # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if not usr or not passwd:
                print("Please Do Not Leave Username or Password as Empty or Space")
                continue

            if usr in db and db[usr] == passwd:
                activity = "LOGIN"
                status = "Success"
            else:
                activity = "LOGIN"
                status = "Failed"
                print("The User Does not Exist Yet. Please Register an Account.")

            log_line = f"\n[{timestamp}] [{activity}] User: {usr}, Status: {status}, IP: {ipAddr}"


            # Append to log file - Logs Appending Block
            with open("logs.txt", "a") as f:
                f.write(log_line)
            #print("Logs Appended: ", log_line)

            # If we break since the first Success, the logs won't append since the break is above the Logs Appending Block
            if status == "Success":
                break

        # Accessing Files
        while True:
            file_accessing = input("===Choose File=== \n [1. Kali Linux Documentation]\n [2. Company Audit Report]\n [3. HR Documents]\n [4. Budget Plan]\n>>> ").strip()
            if not file_accessing:
                print("Please Do Not Leave Username or Password as Empty or Space")
                continue
            
            if file_accessing in ["1","2","3","4" ]:
                activity = "FILE ACCESS"
                status = "Success"
            else:
                activity = "FILE ACCESS"
                status = "Failed"
                print("Choose File Again")

            
            log_line = f"\n[{timestamp}] [{activity}] User: {usr}, Status: {status}, IP: {ipAddr}"
            with open("logs.txt", "a") as f:
                f.write(log_line)

            if status == "Success":
                break
        
        # Log out
        while True:
            usr_logout = input("That's all for today. Do you want to log out? (yes/no): ").lower()

            if usr_logout == "no":
                if_User_db_isNotEmpty()  
            elif usr_logout == "yes":
                activity = "LOGOUT"
                status = "Success"

                log_line = f"\n[{timestamp}] [{activity}] User: {usr}, Status: {status}, IP: {ipAddr}"

                # Append to log file - Logs Appending Block
                with open("logs.txt", "a") as f:
                    f.write(log_line)
            break
        break

main()