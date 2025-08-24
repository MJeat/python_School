from tkinter import *

# Create the main application window
window = Tk()
window.title("Choosing Food Options")
window.geometry("600x600")

def select_option():
    selected_value = var.get()
    print(selected_value)

# Create a StringVar to hold the value of the selected radio button
var = StringVar()

# Create a frame to hold the radio buttons horizontally
frame = Frame(window)
frame.pack(pady=20)

# Create radio buttons and pack them into the frame
radio_button1 = Radiobutton(frame, text="Option 1", variable=var, value="option1")
radio_button2 = Radiobutton(frame, text="Option 2", variable=var, value="option2")
radio_button3 = Radiobutton(frame, text="Option 3", variable=var, value="option3")

radio_button1.pack(side="left", padx=10)
radio_button2.pack(side="left", padx=10)
radio_button3.pack(side="left", padx=10)

# Create a button that calls the select_option function when pressed
button = Button(window, text="Select", command=select_option)
button.pack(pady=20)

# Start the Tkinter event loop to keep the window open
window.mainloop()
