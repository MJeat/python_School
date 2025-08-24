from tkinter import *





def submit():
    correct_guesses = 0
    selected_value1 = x.get()[0]  # Get only the first character (e.g., "A")
    selected_value2 = y.get()[0] 
    selected_value3 = z.get()[0] 

    Guesses_label.config(text='Guesses: ' + selected_value1 + ", "+  selected_value2 + ", "+  selected_value3, font=("consolas", 20)  )
    Answers_label.config(text="Answers: A, B ,C", font=("consolas", 20))

    if selected_value1 == "A":
        correct_guesses +=1

    if selected_value2 =="B":
        correct_guesses +=1

    if selected_value3 == "C":
        correct_guesses +=1

    score(correct_guesses)


def score(correct_guesses):

    if correct_guesses == 3:
        Result_label.config(text='Result: 3 out of 3',font=("consolas", 20))
    if correct_guesses == 2:
        Result_label.config(text='Result: 2 out of 3',font=("consolas", 20))

    if correct_guesses == 1:
        Result_label.config(text='Result: 1 out of 3',font=("consolas", 20))
    
    if correct_guesses == 0:
        Result_label.config(text='Result: 0 out of 3',font=("consolas", 20))
    

    


# Or use this instead, but longer:
#correct_answer1 = Answer_list[0][0]  #This is when to call an index in the main list. And to call the first element within the first index within the main list. 
           
    #if selected_value == correct_answer1:
     #   Answers_label.config(text="Answers: Well done", font=("consolas", 20))
    
    #else:
     #   Answers_label.config(text="Answers: Wrong", font=("consolas", 20))
    # print(selected_value)



def restart():
    x.set("")
    y.set("")
    z.set("")



    Result_label.config(text="Result: ", font=("consolas", 20))
    Guesses_label.config(text="Guesses: ", font=("consolas", 20))
    Answers_label.config(text="Answers: ", font=("consolas", 20))
    
                

    

# ---------------------------------------------------------------
window = Tk()
window.title("Quiz Game")
#window.geometry("600x600")

correct_answer = {"What is the size of the moon?":"A",
                  "Why do we breath?":"B",
                  "How to swim?":"C"
                  
           }


questions = {"What is the size of the moon?":["A. 234m", "B. 435m", "C. 342m"],
             "Why do we breath?":["A. Oxygen", "B. Live", "C. To see you"],
             "How to swim?":["A. Hand movement", "B. Legs movement", "C. Both hands and legs"]
             }




Answer_list = [["A. 234m", "B. 435m", "C. 342m"],
                ["A. Oxygen", "B. Live", "C. To see you"],
                ["A. Hand movement", "B. Legs movement", "C. Both hands and legs"]
                ]

#-----------------------------------------------------------------------------------------------------
#Question 1:
x = StringVar()


Question1 = Label(window, text='1. What is the size of the moon?', font=("consolas", 20))
Question1.pack(side="top", anchor='w', padx=20)

for index1, answer1 in enumerate(Answer_list[0]):
    radiobutton1 = Radiobutton(window, text=answer1, variable=x, value=answer1, padx=25, font=("consolas", 10))
    radiobutton1.pack(anchor=W)



#-----------------------------------------------------------------------------------------------------
#Question 2:

y = StringVar()

Question2 = Label(window , text="2. Why do we breath?", font=("consolas", 20))
Question2.pack(side="top", anchor="w",padx=20)

for index2, answer2 in enumerate(Answer_list[1]):
    radiobutton2 = Radiobutton(window, text=answer2, variable=y, value=answer2, padx=25, font=("consolas", 10))
    radiobutton2.pack(anchor=W)


#-----------------------------------------------------------------------------------------------------
#Question 3:
z = StringVar()


Question3 = Label(window, text="3. How to swim?", font=("consolas", 20))
Question3.pack(side="top", anchor="w", padx=20)

for index3, answer3 in enumerate(Answer_list[2]):
    radiobutton3 = Radiobutton(window, text=answer3, variable=z, value=answer3, padx=20,font=("consolas", 10))
    radiobutton3.pack(anchor=W)



# ---------------------------------------------------------------

Quit_button = Button(window, text="Quit", font=("consolas", 8), command=window.destroy)
Quit_button.pack(side="bottom")

Restart_button = Button(window, text="Restart", font=("consolas", 15), command=restart)
Restart_button.pack(side="bottom")

Submit_button = Button(window, text="Submit", font=("consolas", 20), command=submit)
Submit_button.pack(side="bottom")


# ---------------------------------------------------------------

Result_label = Label(window, text="Result: ", font=("consolas", 20))
Result_label.pack(side="bottom", anchor='w', padx=20)

Guesses_label = Label(window, text="Guesses: ", font=("consolas", 20))
Guesses_label.pack(side="bottom", anchor='w', padx=20)

Answers_label = Label(window, text="Answers: ", font=("consolas", 20))
Answers_label.pack(side="bottom", anchor='w', padx=20)





window.mainloop()


# What to do next:
    # Perhaps, let the system check all the circles first then click submit to have an overall calculation. No need to select one by one to see which is correct
    # test the Answer, Guesses, and the Result with numbers first before adding more questions
    # Note: u can only choose one answer among 6 other radiobuttons. Need to change this ASAP  


    # IN that case, check ChatGPT chat named "Check Code Here U IDIOT" to add more StringVar to fix this problem above 