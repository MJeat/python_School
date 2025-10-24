import pickle


def main():
    # Asking for User's info
    usrInfo()
    
    # For seeing what's inside the binary file
    #binaryFileOpening()

    # For Clearing the data within the binary file
    #binaryFileClear()


def usrInfo():
    usrname = input("Please Enter Your Username: ")
    passwd = input("Password: ")
    try:
        age = int(input("Age: "))
        phoneNum = input("Phone Number: ")
    except Exception as e:
        print("Something Went Wrong")
    
    addr = input("Address: ")
    binaryFileStoring(usrname, passwd, age, phoneNum, addr)

def binaryFileStoring(usrname, passwd, age,phoneNum, addr):
    with open("binaryFile2.bin","wb") as storing:
        pickle.dump(usrname, storing)
        pickle.dump(passwd, storing)
        pickle.dump(age, storing)
        pickle.dump(phoneNum, storing)
        pickle.dump(addr, storing)

def binaryFileOpening():
    print("=====LOADING DATA=====")
    with open("binaryFile2.bin","rb") as opening:
        while True:
            try:
                obj = pickle.load(opening)
                print(obj)
            except EOFError:
                break

def binaryFileClear():
    with open("binaryFile2.bin","wb"):
        pass

main()

