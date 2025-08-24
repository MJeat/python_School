from tkinter import *

class Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Conversion")
        self.root.geometry('400x400')

        self.create_widgets()

    def create_widgets(self):
        label_number = Label(self.root, text="Enter the number:")
        label_number.grid(row=0, column=0, padx=10, pady=5)

        self.entry_number = Entry(self.root)
        self.entry_number.grid(row=0, column=1, padx=10, pady=5)

        self.choice = StringVar(value="1")

        rb1 = Radiobutton(self.root, text="Binary to Decimal", variable=self.choice, value="1")
        rb1.grid(row=1, column=0, columnspan=2, padx=10, pady=2, sticky="w")

        rb2 = Radiobutton(self.root, text="Decimal to Binary", variable=self.choice, value="2")
        rb2.grid(row=2, column=0, columnspan=2, padx=10, pady=2, sticky="w")

        rb3 = Radiobutton(self.root, text="Hexadecimal to Octal", variable=self.choice, value="3")
        rb3.grid(row=3, column=0, columnspan=2, padx=10, pady=2, sticky="w")

        rb4 = Radiobutton(self.root, text="Hexadecimal to Binary", variable=self.choice, value="4")
        rb4.grid(row=4, column=0, columnspan=2, padx=10, pady=2, sticky="w")

        rb5 = Radiobutton(self.root, text="Binary to Hexadecimal", variable=self.choice, value="5")
        rb5.grid(row=5, column=0, columnspan=2, padx=10, pady=2, sticky="w")

        button_convert = Button(self.root, text="Convert", command=self.convert)
        button_convert.grid(row=6, column=1, pady=10)

        label_result = Label(self.root, text="Result:")
        label_result.grid(row=7, column=0, padx=10, pady=5)

        self.entry_result = Entry(self.root, state="readonly")
        self.entry_result.grid(row=7, column=1, padx=20, pady=5)

        close_button = Button(self.root, text='Close', bg='red', command=self.root.destroy)
        close_button.grid(row=8, column=1, pady=10)

    def convert(self):
        num = self.entry_number.get()
        result = ""

        if self.choice.get() == "1":
            if self.is_valid_binary(num):
                result = self.binary_to_decimal(num)
            else:
                result = "Invalid Binary (0 & 1 only)"
        elif self.choice.get() == "2":
            if self.is_valid_decimal(num):
                result = self.decimal_to_binary(num)
            else:
                result = "Invalid Decimal"
        elif self.choice.get() == "3":
            if self.is_valid_hexadecimal(num):
                result = self.hexadecimal_to_octal(num)
            else:
                result = "Invalid Hexadecimal"
        elif self.choice.get() == "4":
            if self.is_valid_hexadecimal(num):
                result = self.hexadecimal_to_binary(num)
            else:
                result = "Invalid Hexadecimal"
        elif self.choice.get() == "5":
            if self.is_valid_binary(num):
                result = self.binary_to_hexadecimal(num)
            else:
                result = "Invalid Binary"
        
        self.entry_result.config(state="normal")
        self.entry_result.delete(0, END)
        self.entry_result.insert(0, result)
        self.entry_result.config(state="readonly")

    def binary_to_decimal(self, binary_str):
        return str(int(binary_str, 2))

    def decimal_to_binary(self, decimal_num):
        return bin(int(decimal_num))[2:]

    def hexadecimal_to_octal(self, hex_str):
        return oct(int(hex_str, 16))[2:]

    def hexadecimal_to_binary(self, hex_str):
        return bin(int(hex_str, 16))[2:]

    def binary_to_hexadecimal(self, binary_str):
        return hex(int(binary_str, 2))[2:]

    def is_valid_binary(self, binary_str):
        return all(char in '01' for char in binary_str)

    def is_valid_decimal(self, decimal_str):
        return decimal_str.isdigit()

    def is_valid_hexadecimal(self, hex_str):
        return all(char in '0123456789abcdefABCDEF' for char in hex_str)


# Create the Tkinter application
root = Tk()
app = Converter(root) # You call the class using root as an argument to create the GUI
root.mainloop()
