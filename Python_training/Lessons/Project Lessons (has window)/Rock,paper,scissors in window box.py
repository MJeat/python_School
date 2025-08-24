from tkinter import *
import random 

game = ["rock", "paper", "scissors"]

def new_game():
    computer = random.choice(game)
    player = None
    while player not in game:
        player = input("Choose rock, paper, or scissors: ").lower()

    print("Player: ", player)
    print("Computer: ", computer)

    if (player == 'rock' and computer == 'scissors') or \
       (player == 'scissors' and computer == 'paper') or \
       (player == 'paper' and computer == 'rock'):
        print("Player wins!")
    elif player == computer:
        print("Tie!")
    else:
        print("Computer wins!")

def play_again():
    while True:
        play_again = None
        options = ["no", "yes"]
        while play_again not in options:
            play_again = input("Play again? (yes/no): ").lower()

            if play_again in options:
                break
        if play_again == "yes":
            return True
        else:
            print("Come again, sucker!")
            return False

window = Tk()
window.title("Rock, Paper, Scissors")

label = Label(window, text="  Begin! ", font=("consolas", 30))
label.pack(side="top")



computer_label = Label(window, text=" Player          Computer", font=("consolas", 15))
computer_label.pack(fill=BOTH, expand=True) # fill = BOTH means that the label will expand both horizontally and vertically if the window resizes.
                                                # expand = True means that the expansion of fill will be executed. If false, no. This only works with fill



# Adjust the position of the question mark PLAYER label
player_answer = Label(window, text="     ", font=("consolas", 20))
player_answer.pack(side='left')
player_answer = Label(window, text="?", font=("consolas", 20))
player_answer.pack(side='left')

# Adjust the position of the question mark COMPUTER label
computer_answer = Label(window, text="     ", font=("consolas", 20))
computer_answer.pack(side='right')
computer_answer = Label(window, text="?", font=("consolas", 20))
computer_answer.pack(side='right')



quit_button = Button(window, text="Quit", font=("consolas", 10), command=window.destroy)
quit_button.pack(side="bottom")
restart_button = Button(window, text="Restart", font=("consolas",15))
restart_button.pack(side="bottom")



# Adding a vertical line separator using Canvas
canvas = Canvas(window, bd=0, highlightthickness=0)
canvas.pack(side="top", fill=BOTH, expand=True)

def draw_line(event):
    canvas.delete("all")
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    canvas.create_line(canvas_width//2, 0, canvas_width//2, canvas_height, fill='black')

    computer_label.pack_configure(anchor="w" if event and event.width > 1 else "e")
    
   

canvas.bind("<Configure>", draw_line)

frame = Frame(window)
frame.pack(side="top", fill=BOTH, expand=True)

while True:
    new_game()
    if not play_again():
        break

window.mainloop()


# ok changing plan. Look at your notepad for this project.