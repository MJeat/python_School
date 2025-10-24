# import pickle
# import os # using os here is to check file existence and size in the system


# def main():
#     while True:
#         print("\n===== MENU =====")
#         print("1. Input Data")
#         print("2. Read Data")
#         print("3. Exit")

#         choice = input("Enter choice (1/2/3): ").strip()

#         if choice == "1":
#             usrInfo()
#         elif choice == "2":
#             binaryFileOpening()
#         elif choice == "3":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice, try again.")


# def usrInfo():
#     while True:
#         print("\n=== Input User Data ===")
#         usrname = input("Please Enter Your Username (or 'b' to go back): ").strip()
#         if usrname.lower() == "b":
#             break

#         passwd = input("Password: ").strip()
#         try:
#             age = int(input("Age: ").strip())
#             phoneNum = input("Phone Number: ").strip()
#         except ValueError:
#             print("Invalid input for age! Try again.")
#             continue

#         addr = input("Address: ").strip()

#         binaryFileStoring(usrname, passwd, age, phoneNum, addr)


# def binaryFileStoring(usrname, passwd, age, phoneNum, addr):
#     with open("binaryFile2.bin", "ab") as storing:  # Append instead of overwrite. This is a better way to store data. We use dictionary
#         data = {
#             "Username": usrname,
#             "Password": passwd,
#             "Age": age,
#             "Phone": phoneNum,
#             "Address": addr
#         }
#         pickle.dump(data, storing)
#     print("Data saved successfully!")


# def binaryFileOpening():
#     print("\n===== LOADING DATA =====")
#     if not os.path.exists("binaryFile2.bin") or os.path.getsize("binaryFile2.bin") == 0:
#         print("No data found. Please input data first.")
#         return

#     with open("binaryFile2.bin", "rb") as opening:
#         while True: # classic way to read until 
#             try:
#                 obj = pickle.load(opening)
#                 print(obj)
#             except EOFError: # End Of File = EOF, this part is to stop the loop when reaching the end of the file
#                 break


# main()





import pandas as pd
import os


def main():
    while True:
        print("\n===== MENU =====")
        print("1. Input Data")
        print("2. Read Data")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            usrInfo()
        elif choice == "2":
            readCSV()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


def usrInfo():
    while True:
        print("\n=== Input User Data ===")
        usrname = input("Please Enter Your Username (or 'b' to go back): ").strip()
        if usrname.lower() == "b":
            break

        passwd = input("Password: ").strip()
        try:
            age = int(input("Age: ").strip())
            phoneNum = input("Phone Number: ").strip()
        except ValueError:
            print("Invalid input for age! Try again.")
            continue

        addr = input("Address: ").strip()

        storeCSV(usrname, passwd, age, phoneNum, addr)


def storeCSV(usrname, passwd, age, phoneNum, addr):
    data = {
        "Username": [usrname],
        "Password": [passwd],
        "Age": [age],
        "Phone": [phoneNum],
        "Address": [addr]
    }
    df = pd.DataFrame(data) # using pandas here

    file_exists = os.path.exists(r"C:\Users\User\OneDrive - American University of Phnom Penh\Desktop\python_school\ComputerScienceB\PythonFileHandling\data.csv")

    # append if exists, else create new file if not yet exists
    df.to_csv(r"C:\Users\User\OneDrive - American University of Phnom Penh\Desktop\python_school\ComputerScienceB\PythonFileHandling\data.csv", mode="a", header=not file_exists, index=False)

    print("Data saved successfully to data.csv!")


def readCSV():
    print("\n===== LOADING DATA =====")
    if not os.path.exists(r"C:\Users\User\OneDrive - American University of Phnom Penh\Desktop\python_school\ComputerScienceB\PythonFileHandling\data.csv") or os.path.getsize(r"C:\Users\User\OneDrive - American University of Phnom Penh\Desktop\python_school\ComputerScienceB\PythonFileHandling\data.csv") == 0:
        print("No data found. Please input data first.")
        return

    df = pd.read_csv(r"C:\Users\User\OneDrive - American University of Phnom Penh\Desktop\python_school\ComputerScienceB\PythonFileHandling\data.csv")
    print(df)


main()
