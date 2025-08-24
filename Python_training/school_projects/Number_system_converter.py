from tkinter import *


def binary_to_decimal(binary_str):
    return str(int(binary_str, 2))

def decimal_to_binary(decimal_num):
    return bin(int(decimal_num))[2:]

def hexadecimal_to_octal(hex_str):
    return oct(int(hex_str, 16))[2:]

def hexadecimal_to_binary(hex_str):
    return bin(int(hex_str, 16))[2:]

def binary_to_hexadecimal(binary_str):
    return hex(int(binary_str, 2))[2:]


def convert():
    num = entry_number.get() 
    result = ""

    if choice.get() == "1":
        if is_valid_binary(num):
            result = binary_to_decimal(num)
        else:
            result = "Invalid Binary (0 & 1 only)"
    elif choice.get() == "2":
        if is_valid_decimal(num):
            result = decimal_to_binary(num)
        else:
            result = "Invalid Decimal"
    elif choice.get() == "3":
        if is_valid_hexadecimal(num):
            result = hexadecimal_to_octal(num)
        else:
            result = "Invalid Hexadecimal"
    elif choice.get() == "4":
        if is_valid_hexadecimal(num):
            result = hexadecimal_to_binary(num)
        else:
            result = "Invalid Hexadecimal"
    elif choice.get() == "5":
        if is_valid_binary(num):
            result = binary_to_hexadecimal(num)
        else:
            result = "Invalid Binary"
    
    entry_result.config(state="normal") 
    entry_result.delete(0, END) 
    entry_result.insert(0, result) 
    entry_result.config(state="readonly")  


def is_valid_binary(binary_str):
    return all(char in '01' for char in binary_str)

def is_valid_decimal(decimal_str):
    return decimal_str.isdigit()

def is_valid_hexadecimal(hex_str):
    return all(char in '0123456789abcdefABCDEF' for char in hex_str)




root = Tk()
root.title("Number Conversion")
root.geometry('400x400')

label_number = Label(root, text="Enter the number:")
label_number.grid(row=0, column=0, padx=10, pady=5)

entry_number =Entry(root)
entry_number.grid(row=0, column=1, padx=10, pady=5)

choice = StringVar(value="1") 


rb1 = Radiobutton(root, text="Binary to Decimal", variable=choice, value="1")
rb1.grid(row=1, column=0, columnspan=2, padx=10, pady=2, sticky="w")

rb2 = Radiobutton(root, text="Decimal to Binary", variable=choice, value="2")
rb2.grid(row=2, column=0, columnspan=2, padx=10, pady=2, sticky="w")

rb3 = Radiobutton(root, text="Hexadecimal to Octal", variable=choice, value="3")
rb3.grid(row=3, column=0, columnspan=2, padx=10, pady=2, sticky="w")

rb4 = Radiobutton(root, text="Hexadecimal to Binary", variable=choice, value="4")
rb4.grid(row=4, column=0, columnspan=2, padx=10, pady=2, sticky="w")

rb5 = Radiobutton(root, text="Binary to Hexadecimal", variable=choice, value="5")
rb5.grid(row=5, column=0, columnspan=2, padx=10, pady=2, sticky="w")

button_convert = Button(root, text="Convert", command=convert)
button_convert.grid(row=6, column=1, pady=10)


label_result = Label(root, text="Result:")
label_result.grid(row=7, column=0, padx=10, pady=5)

entry_result = Entry(root, state="readonly", width=25)
entry_result.grid(row=7, column=1, padx=10, pady=5)

Close_button = Button(root, text='close', bg= 'red',command=root.destroy)
Close_button.grid(row=8, column=1, pady=10)

root.mainloop()
