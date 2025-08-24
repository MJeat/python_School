from tkinter import *



def game():


    player_list=[]
    correct_guesses = 0


    for question, answer in correct_answer.items():
        print("---------------------------")
        print(question)


        for option in questions[question]:
            print(option)


        player = input("Choose A, B, C: ").upper()
        while player not in ["A", "B", "C"]:
            player = input("Choose A, B, C: ").upper()

        player_list.append(player)


        if player == answer:
            print("CORRECT")
            correct_guesses +=1
            
            
        else:
            print("WRONG")

    score(correct_guesses, player_list)



def check_answers():
    pass

def score(correct_guesses, player_list ):
    print("---------------------------")
    print("RESULTS")
    print("Answers: ", *correct_answer.values())
    print("Your Guesses: ", *player_list)
    print("Overall Score: {:.2f}".format(correct_guesses / len(player_list)))   # Use format and {:.2f} if you want a certain amount of decimal numbers. 
                                                                                    #In this case, it is 2 numbers after a decimal point "."





def restart():
    while True:
        restart = input("Play agian? (yes/no): ").lower()
        while restart not in ["yes","no"]:
            restart = input("Play agian? (yes/no): ").lower()

        return restart == "yes"
            
            



window = Tk()
window.title("Quiz Game")

correct_answer = {"What is the size of the moon?":"A",
                  "Why do we breath?":"B",
                  "How to swim?":"C"
                  
           }


questions = {"What is the size of the moon?":["A. 234m", "B. 435m", "C. 342m"],
             "Why do we breath?":["A. Oxygen", "B. Live", "C. To see you"],
             "How to swim?":["A. Hand movement", "B. Legs movement", "C. Both hands and legs"]
             }


Answers_label= Label(text="Answers: ", font=("consolas", 10))









Quit_button = Button(window, text="Quit", font=("consolas", 10), command=window.destroy)
Quit_button.grid(row=3, column=2, columnspan=2)

Restart_button = Button(text="Restart", font=("consolas", 15), command=restart)
Restart_button.grid(row=3, column=2, columnspan=2)

Submit_button = Button(text="Submit", font=("consolas", 20), command=check_answers)
Submit_button.grid(row=3, column=2, columnspan=2)



game()

while restart():
    game()
print("GG")





window.mainloop()