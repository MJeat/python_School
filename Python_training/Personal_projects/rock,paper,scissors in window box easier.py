from tkinter import *
import random

def check_winner():  # Submission part
    global game
    global Player_enterybox
    global Computer_choice_label
    global label
    global Winner_label
    
    player_choice = Player_enterybox.get().lower()  # Get the text from Entry widget
   

    Winner_label.config(text="Winner is: ",bg= 'white', font=("consolas", 30), width=30)
    if player_choice not in game:
        Winner_label.config(text="Error: Please enter rock, paper, or scissors only", bg="red", font=("consolas", 10), width=60)
        return
    
    Computer_choice = random.choice(game)
    
    Computer_choice_label.config(text=Computer_choice, font=("consolas", 15))
       

    if (player_choice == 'rock' and Computer_choice == 'scissors') or \
       (player_choice == 'scissors' and Computer_choice == 'paper') or \
       (player_choice == 'paper' and Computer_choice == 'rock'):
        Winner_label.config(text="Winner is: Player!",bg="light green", font=("consolas", 15))
        
    elif player_choice == Computer_choice:
        Winner_label.config(text="Winner is: No one! A Tie!",bg="yellow" ,font=("consolas", 15))
        
    else:
        Winner_label.config(text="Winner is: Computer!",bg="orange", font=("consolas", 15))
        
        

def Restart():  # Like clearing computer choice and player input and restart the check winner again. Also, check to not let computer choice reveal before player input. 
                                        # it should be after the check winner executed
    global Player_enterybox
    global Computer_choice
    global Winner_label
    global Computer_choice_label
    
    # Clear player's input
    Player_enterybox.delete(0, END)

    
    # Reset Winner_label
    Winner_label.config(text="Winner is: ",bg= 'white', font=("consolas", 15), width=30)
    Computer_choice_label.config(text=" " )
    
    # Reset Computer_choice (not displayed until player submits)
    Computer_choice = None


window = Tk()
window.title("Rock, Paper, Scissors")

game = ["rock", "paper", "scissors"]

label = Label(window, text="Begin!", font=("consolas", 30))
label.grid(row=0, column=0, columnspan=2)

Player = Label(window, text='Player Turn: ', font=("consolas", 15), width=20)
Player.grid(row=1, column=0)


Player_enterybox = Entry(window)
Player_enterybox.grid(row=1, column=1)



Computer_choice_label = Label(window, text="", font=("consolas", 15))
Computer_choice_label.grid(row=2, column=1)


Computer_label = Label(window, text="Computer: ", font=("consolas", 15))
Computer_label.grid(row=2, column=0)



Winner_label = Label(window, text='Winner is: ',bg= 'white', font=("consolas", 15), width=30)
Winner_label.grid(row=3, column=0, columnspan=2)

Submit_button = Button(window, text='Submit', font=('consolas', 15), command=check_winner)
Submit_button.grid(row=6, column=0, columnspan=3)  # Check winner

Restart_button = Button(window, text='Restart', font=('consolas', 11), command=Restart)
Restart_button.grid(row=7, column=0, columnspan=3)  # Restart

Quit_button = Button(window, text='Quit', font=('consolas', 8), command=window.destroy)
Quit_button.grid(row=8, column=0, columnspan=3)  # Quit (Auto)

window.mainloop()

# In Tkinter (and many GUI frameworks), when you create widgets like Label, Entry, or Button, 
# you should avoid calling grid() or pack() immediately after the widget creation in the same line where you assign the widget to a variable.
# so i shouldnt add .grid() or .pack() immediately after as it will return None. So, just enter and write .grid() afterwards
