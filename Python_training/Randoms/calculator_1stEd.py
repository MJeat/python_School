from tkinter import *

def clicked_button(value):
    current_text = result_box['text']

    if current_text == 'Result Here':
        result_box.config(text=value)
    # else
    #     result_box.config




window = Tk()
window.title('1st Ed Calculator')
window.geometry('500x500')


frame =Frame(window)
frame.pack(expand=True, fill='both')

for i in range(1,6):
    frame.grid_columnconfigure(i, weight=1)

for j in range(1,6):
    frame.grid_rowconfigure(j, weight=1)



result_box = Label(frame, text='Result Box', font=('consolas', 20), bg='light grey', anchor='e')
result_box.grid(row=1,column=1, columnspan=5, sticky='nsew')

buttons = [
    ('7', 2, 1),('8', 2, 2),('9', 2, 3),
    ('4', 3, 1),('5', 3, 2),('6', 3, 3),
    ('1', 4, 1),('2', 4, 2),('3', 4, 3),
]

for button in buttons:
    text, row, col = button[:3]
    command = button[3] if len(button) > 3 else lambda t=text: clicked_button(t)
    Button(frame, text=text, font=("consolas", 20), command=command).grid(row=row, column= col, sticky='nsew' )
    



window.mainloop()