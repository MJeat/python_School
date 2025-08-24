from tkinter import *
#grid() = geometry manager that organizes widgets in a table-like structure in a parent widget
# When you use pack(), it usually place on top of each other, creating a long line down


# row is horizontal, whereas column is vertical. 

window = Tk()

title_label = Label(window, text='Sign Up ', font=("Arial", 20)).grid(row=0, column=0, columnspan=2)


first_name = Label(window, text="First Name: ", width=20).grid(row=1, column=0) 
first_nameEntry = Entry(window).grid(row=1, column=1)

last_name = Label(window, text="Last Name: ").grid(row=2, column=0)
last_nameEntry = Entry(window).grid(row=2, column=1)

Email = Label(window, text="Email: ").grid(row=3, column=0)
EmailEntry = Entry(window).grid(row=3, column=1)

submit = Button(window, text='Submit', font=("consolas", 10)).grid(row=6,column=0, columnspan=2) # columnspan=2 means that it will move 2 columns to the right



window.mainloop()