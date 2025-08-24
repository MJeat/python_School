from tkinter import *
import math


def calculation():
    radius = float(entery.get())
    if radius < 0:
        Result.config( text="No negative number", font=("consolas", 40)) 
    
    else:
        area = radius  **2 * math.pi
        Result.config( text=f'Result: {area:.3f}', font=("consolas", 40)) 





window= Tk()
window.geometry("600x300")
window.title("Circle Area Calculator")


Enter = Label(window, text="Enter you Radius", font=("consolas", 30))
Enter.pack()

entery = Entry(window)
entery.pack()



calculate_button = Button(window, text="Calculate the area", font=("consolas", 20), command=calculation)
calculate_button.pack(pady= 20)

close_button = Button(window, text="X", font=("consolas", 10), bg="RED", command=window.destroy)
close_button.place(x=580, y=0)

Result = Label(window, text="Result: ", font=("consolas", 40))
Result.pack()


window.mainloop()
