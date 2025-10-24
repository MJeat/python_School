from urllib import request
import pickle

'''
    In Python, the second argument in the open() function is the file mode. It tells Python how you want to open the file. Here are the most common modes:

    Mode	Meaning
    'r'	Read (default). File must exist.
    'w'	Write. Creates new or overwrites file.
    'a'	Append. Adds to end of file if it exists.
    'x'	Create. Fails if file exists.
    'b'	Binary mode (e.g., 'rb', 'wb').
    't'	Text mode (default, e.g., 'rt').
    '+'	Read and write (e.g., 'r+', 'w+').
    You can combine them, for example:

    'rb' = read binary
    'w+' = write and read
'''


def main():
    #basic()
    #retrievingFromWeb()
    binaryFile()

def basic():
    # Retrieving text From one File
    try:
        with open(r"C:\Users\User\OneDrive - American University of Phnom Penh\Desktop\python_school\ComputerScienceB\playground.py","r") as f:
            content = f.read()
            print(content)
    except Exception as e:
        print("There's something wrong with the damn code bruh. Here's your input file location: ")
        print(e)

    # Appending New Text From one File
    try:
        text2 = "text2= \"Well, this is an additional text\""
        with open(r"C:\Users\User\OneDrive - American University of Phnom Penh\Desktop\python_school\ComputerScienceB\playground.py","a") as f:
            f.write(text2)
    except Exception as d:
        print("There's something wrong with the damn code bruh. Here's your input file location: ")
        print(d)


    print("The Program is still continuing")

def retrievingFromWeb():
    # You gotta import request from urllib
    try:
        url = "https://gutenberg.org/cache/epub/1513/pg1513.txt"
        response = request.urlopen(url)
        raw = response.read().decode('utf8')
        print(raw[:500])
    except Exception as e:
        print("Failed to retrieve web page:")
        print(e)

# Writing to a Binary File
def writingBinaryFile():
    with open("binaryFile.bin","wb") as file:
        pickle.dump("Hello World", file)
        pickle.dump(67, file)
        pickle.dump([1,2,3,4,5],file)
    file.close() # This is unneccessary because we are using with open(). Can be removed
    
# Opening the Binary File
def openingBinaryFile():
    with open("binaryFile.bin", "rb") as opening:
        while True:
            try:
                obj = pickle.load(opening)
                print(obj)
            except EOFError:
                break
    opening.close() # This is unneccessary because we are using with open(). Can be removed

def binaryFile():
    # You need to import pickle
    # Calling functions
    writingBinaryFile()
    openingBinaryFile()

main()