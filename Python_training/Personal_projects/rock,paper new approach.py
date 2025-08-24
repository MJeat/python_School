

from tkinter import *
import random


def check_answer(event=None):
    global game
    global Player_input
    global Choose
    global Blank_computer_label

    player_choice = Player_input.get().lower()
    Computer = random.choice(game)
    Blank_computer_label.config( text=Computer, font=('consolas', 20))
    Blank_computer_label.grid(row=2, column=1)

    


    if (player_choice == 'rock' and Computer == 'paper') or \
    (player_choice == 'paper' and Computer == 'scissors') or \
    (player_choice == 'scissors' and Computer == 'rock'):
        Choose.config(text='Computer Wins!', font=('consolas', 20), bg= "Orange", width= 45 )
        Player_input.delete(0, END)
        Blank_computer_label.config(text=' ', font=('consolas', 20))

    elif player_choice == Computer:
        Choose.config(text='A tie!', font=('consolas', 20), bg= "Yellow",  width= 45 )
        Player_input.delete(0, END)
        Blank_computer_label.config(text=' ', font=('consolas', 20))

    elif player_choice not in game:
        Choose.config(text='Enter rock, paper or scissors only', font=('consolas', 20), bg= "Red", width= 45)
        Player_input.delete(0, END)
        Blank_computer_label.config(text=' ', font=('consolas', 20))
        
 
    else:
        Choose.config(text='Player Wins!', font=('consolas', 20), bg= "Green", width=45 )
        Player_input.delete(0, END)
        Blank_computer_label.config(text=' ', font=('consolas', 20))



    
# I dont need restart() function since I already use the:
    # Player_input.delete(0, END)
    # Blank_computer_label.config(text=' ', font=('consolas', 20)) 


"""
def restart():
    global game
    global Player_input
    global Choose
    global Computer

    Player_input.delete(0, END)
    Computer = None

"""


window = Tk()
window.title("Rock, Paper, Scissors")
game = ["rock", "paper", "scissors"]


Play_label = Label(window, text='Play!', font=('consolas', 50))
Play_label.grid(row=0, column=0, columnspan=5)
# ------------------------------------

Player_label = Label(window, text='Player: ', font=('consolas', 20))
Player_label.grid(row=1, column=0)

Player_input = Entry(window)
Player_input.grid(row=1, column=1)
Player_input.bind("<Return>", check_answer) # for when you click enter on keyboard and it works without having to click the submit button in the tab.
                                            # you also need to put event= None in the check() function


Computer_label = Label(window, text='Computer: ', font=('consolas', 20))
Computer_label.grid(row=2, column=0)
Blank_computer_label = Label(window, text='', font=('consolas', 20))
Blank_computer_label.grid(row=2, column=1)

# ------------------------------------

Choose = Label(window, text='Enter rock, paper or scissors', font=('consolas', 15), bg= 'white')
Choose.grid(row=3, column=0, columnspan=5, pady=10)

Submit_button = Button(window, text='Submit', font=('consolas', 20), command=check_answer)
Submit_button.grid(row=4, column=0, columnspan=5)

# Restart_button = Button(window, text='Restart', font=('consolas', 15), command=restart)
# Restart_button.grid(row=5, column=0, columnspan=5)

Quit_button =Button(window, text='Quit', font=('consolas', 15), command=window.destroy)
Quit_button.grid(row=5, column=0, columnspan=5)



window.mainloop()