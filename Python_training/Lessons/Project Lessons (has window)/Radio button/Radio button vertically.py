from tkinter import *

from PIL import Image, ImageTk  # Import Pillow modules for image manipulation

# List of food items
food = ['pizza', 'burger', 'coke']

def order():
    # Function to handle radio button selection
    if x.get() == 0:        # Number 0,1,2 are index for the list of food
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered burger!")
    elif x.get() == 2:
        print("You ordered coke!")
    else:
        print("Huh? What do you want?")

def resize_image(image_path, size):
    # Function to open, resize, and convert an image to PhotoImage
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
    return ImageTk.PhotoImage(image)


window = Tk()
window.title("Choosing a Food vertically")
window.geometry("600x600")

# Resize images to a desired size (e.g., 100x100 pixels)
size = (100, 100)
pizzaImage = resize_image("pizza.png", size)
burgerImage = resize_image("burger.png", size)
cokeImage = resize_image("coke.png", size)

# List of resized images
foodImages = [pizzaImage, burgerImage, cokeImage]

x = IntVar()  # Variable to hold the selected value of the radio buttons

# Create and pack radio buttons
for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                              text=food[index],  # Adds text to radio buttons
                              variable=x,  # Groups radio buttons together if they share the same variable
                              value=index,  # Assigns each radio button a different value
                              padx=25,  # Adds padding on x-axis
                              font=("Impact", 20),
                              image=foodImages[index],  # Adds image to radio button
                              compound="left",  # Adds image and text (left-side)
                              command=order
                              )  # Sets command of radio button to function
    
    
    radiobutton.pack(anchor=W)  # Pack radio buttons to the window

window.mainloop()  # Start the Tkinter event loop



# This one can do horizontally:

from tkinter import *
from PIL import Image, ImageTk  # Import Pillow modules for image manipulation

# List of food items
food = ['pizza', 'burger', 'coke']

def order():
    # Function to handle radio button selection
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered burger!")
    elif x.get() == 2:
        print("You ordered coke!")
    else:
        print("Huh? What do you want?")

def resize_image(image_path, size):
    # Function to open, resize, and convert an image to PhotoImage
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
    return ImageTk.PhotoImage(image)


window = Tk()
window.title("Choosing a Food horizontally")
window.geometry("1000x300")

# Resize images to a desired size (e.g., 100x100 pixels)
size = (100, 100)
pizzaImage = resize_image("pizza.png", size)
burgerImage = resize_image("burger.png", size)
cokeImage = resize_image("coke.png", size)

# List of resized images
foodImages = [pizzaImage, burgerImage, cokeImage]

x = IntVar()  # Variable to hold the selected value of the radio buttons

# Create a frame to hold the radio buttons horizontally
frame = Frame(window)
frame.pack(pady=20)  # Add padding to the frame if needed

# Create and pack radio buttons horizontally within the frame
for index in range(len(food)):
    radiobutton = Radiobutton(frame, 
                              text=food[index],  # Adds text to radio buttons
                              variable=x,  # Groups radio buttons together if they share the same variable
                              value=index,  # Assigns each radio button a different value
                              padx=25,  # Adds padding on x-axis
                              font=("Impact", 20),
                              image=foodImages[index],  # Adds image to radio button
                              compound="left",  # Adds image and text (left-side)
                              command=order
                              )  # Sets command of radio button to function

    radiobutton.pack(side="left", padx=10)  # Pack radio buttons horizontally within the frame

window.mainloop()  # Start the Tkinter event loop
