from tkinter import *
import random


def next_turn(row, column):
    global player   # It means that the player variable can be accessed and modified from anywhere in the program, not just within this function. Or you can just say use global when the variable is outside the function.
    if buttons[row][column]['text'] == '' and check_winner() is False:    # buttons[row][column]['text']: so it's just checking whether the specific button is displayed or not
        if player == players[0]:  # X's turn                                          # also, it's about if the button is empty, then write these codes below. 
            buttons[row][column]['text'] = player

            if check_winner() is False:     # There are  2 ''if check_winner() is False'' in the next_turn function. This if loop means that if no one wins yet, move on to the next player
                player = players[1]
                label.config(text=(players[1]+ ' Turn'))

            elif check_winner() is True:
                
                label.config(text=(players[0]+ ' Win'))
            elif check_winner() == 'Tie':
                label.config(text='Tie')


        else: # O's turn 
            buttons[row][column]['text'] = player                      # And if the button is not empty (already has x or o), then use this code.
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+ ' Turn'))

            elif check_winner() is True:
                
                label.config(text=(players[1]+ ' Win'))
            elif check_winner() == 'Tie':
                label.config(text='Tie')



def check_winner():
    for row in range(3): # check for straight win for the letter
        if buttons[row][0]['text'] ==  buttons[row][1]['text'] ==  buttons[row][2]['text'] != '':
            return True

    for column in range(3):    
        if  buttons[0][column]['text'] ==  buttons[1][column]['text'] ==  buttons[2][column]['text'] !='':
            return True
        
# Check diagonal win for the letter:
    if  buttons[0][0]['text'] ==  buttons[1][1]['text'] ==  buttons[2][2]['text'] !="":
        return True # Meaning there is winner
    
    elif buttons[0][2]['text'] ==  buttons[1][1]['text'] ==  buttons[2][0]['text'] !="":
        return True
    elif empty_space() is False:    # This line checks if there are no empty spaces left on the board by calling the empty_spaces function. 
                                        #If there are no empty spaces, it indicates that the game is a tie. 
                                        # False here means there is no space left, whereas True if there is empty space left
        return 'Tie'
    else:                   # (*) 
        return False     # Return False if there is no winner and the game is not a tie
                        # If no win condition or tie condition is met, the function returns False, indicating that there is no winner yet and the game continues.

def empty_space():
    spaces = 9
    global player
    for row in range(3):
        for column in range(3):

            if buttons[row][column]['text'] !="":
                spaces -= 1

    if spaces == 0:
        return False    # Stop the game if tie (*) 
    else:
        return True     # Continue if no tie yet. Return True if there is still empty space
 

def new_game():
    global player
    player = random.choice(players)
    
    label.config(text= player + ' Turn')        # Use .config when you need to update the text/ the label

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='')

window = Tk()
window.title("Tic-tac-toe")
players = ['X', 'O']
player = random.choice(players)
buttons = [[0,0,0],               # This is the lines of tic tac toe
           [0,0,0],
           [0,0,0]]



label = Label(text=player+ ' Turn', font=('consolas', 40)) # This makes a label at the top of the window that shows whose turn it is.
label.pack(side='top')    # This puts the label at the top of the window./ # If i want to put it to top left or right, just use direction like northwest: nw. 
                                #Example: label.pack(side='left', anochor= 'nw')                               

quit_button = Button(text='Quit', font=('consolas', 15), command=window.destroy) 
quit_button.pack(side='bottom')

reset_button = Button(text='Restart', font=('consolas', 15), command=new_game) 
reset_button.pack(side='bottom')


frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='' ,font=('consolas', 40),width=5, height=2, command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

# So, buttons[row][column] is just a way to find or put a button in the right box on our Tic-Tac-Toe grid.
# Imagine you have a notebook with a 3x3 grid. You want to draw a circle (button) in one of the boxes. 
# To tell your friend exactly where to draw, you might say, "Draw it in row 2, column 1." That's exactly what buttons[row][column] does with buttons in the grid.
# It's like using coordinates to find a spot on a map - you need to know both the row and the column to know exactly where you're talking about!


# Explain command=lambda... section:
# In simple terms, this line of code is like attaching a little note to each button that says, "When you press me, tell the game I'm the button at row X and column Y!"
# It's a way of making sure your magic wand knows exactly which button you're pointing at, so it can do the right thing when you click it!
# so it precisely tell where to mark x or o in the box


# In a Tic-Tac-Toe game (or X.O game), using the .grid(row=row, column=column) method helps in creating the layout 
# where each cell (or button) of the 3x3 grid is correctly positioned. 

window.mainloop()       # This keeps the window open so we can play the game and interact with it.

