
from tkinter import * 
import random


Amount_of_questions = 0

def Restart():
    global Amount_of_questions
    Amount_of_questions = 0
    Asked_question.config(state=NORMAL)

    Question = random.choice(questions)
    Asked_question.config(text=Question)


def Next():
    global Amount_of_questions   
    Amount_of_questions += 1

    if Amount_of_questions <= 10:

        Question = random.choice(questions)
        Asked_question.config(text=Question)
    else:
        Asked_question.config(text="That's all for IELTS speaking part 1. You may now move to part 2.")
        Asked_question.config(state=DISABLED)

questions = [
    "What is your (full) name?",
    "Can I have your name please?",
    "Could you tell me your full name please?",
    "What shall I call you?",
    "How can I address you?",
    "Does your name have any special meaning?",
    "Is your name important to you?",
    "Do Korean people like changing their name? Why?",
    "Have you ever changed your name? Why or why not?",
    "Why do so many people change their name?",
    "Do you work or study?",
    "What are you studying?",
    "What’s your major?",
    "Why did you choose that subject?",
    "What do you find most interesting about your course?",
    "What is your favorite subject?",
    "What do you dislike about your study?",
    "What do you hope to do after your graduation?",
    "What are your ambitions for the future?",
    "Do you hope to gain any qualifications?",
    "What are the advantages of studying instead of working?",
    "Can you describe your job to me?",
    "What do you do for a living?",
    "How long have you been doing it?",
    "Can you describe one of your typical working days?",
    "What’s your daily routine on a working day?",
    "Why did you choose to do that job?",
    "What things do you enjoy about your work? Why?",
    "What do you think is the attraction of your work?",
    "What is your ideal job?",
    "Do you want to change your current job? Why or why not?",
    "Are you willing to keep your job permanently?",
    "What are your plans for the future?",
    "Can you describe your town or village to me?",
    "Tell me something about your hometown.",
    "Where are you from?",
    "Where is your hometown?",
    "Where do you come from?",
    "What is the name of the street you live on?",
    "What kind of street do you live on?",
    "What do you like about your town?",
    "What is the weather like in your town?",
    "What building is considered famous in your town?",
    "What jobs do people in your town do?",
    "How has your town changed over the last twenty years?",
    "What changes have taken place in your city in recent years?",
    "Do you think it is better to live in the center of town or outside in the country? Why?",
    "What do you enjoy doing in your free time?",
    "How much time do you have each week for doing these things?",
    "Why do you like doing these activities?",
    "How did you start doing this activity at first?",
    "Is there some other hobby or sport you would like to try? Why?",
    "How has the way people spend their free time changed over the years?",
    "What do you do when you have a holiday?",
    "Who do you usually spend holiday with?",
    "Where do you like to spend your holidays? Why?",
    "Can you describe a typical day in your holidays?",
    "Why are holidays and important to you?",
    "If you could take a holiday anywhere in the world, where would you go? Why?",
    "What do people usually do during holidays and in your town?",
    "What do people do in your town in their free time?",
    "Where can they go out for entertainment, or to enjoy themselves?",
    "Which do you prefer: eating in restaurants or eating at home?",
    "Which are the best places to eat out?",
    "How did you come here today?",
    "What is public transport like in your town?",
    "How do you think it could be improved?",
    "Do you think people should use public transport more? Why (not)?",
    "How much time do you spend shopping every week?",
    "Do you enjoy going shopping? Why (not)?",
    "What is your favourite shop and why do you like it?",
    "What problems are there with shopping in your area?",
    "Can you describe the house where you live to me?",
    "What is there to do in the area where you live?",
    "What do you like about the area where you live?",
    "How do you think it could be improved?",
    "Do you think it is better to live in the centre of town or outside in the country? Why?",
    "Do you enjoy reading? Why?",
    "What sort of things do you read?",
    "Tell me something about your favourite book.",
    "What are the advantages of reading instead of watching television or going to the cinema?",
    "What sports are most popular in your country?",
    "What sports and games did you most enjoy playing when you were a child?",
    "Do people take as much exercise as in the past?",
    "Why is exercise good for you?"
]

window = Tk()
window.title("Questions for IELTS speaking part 1")
window.geometry("1000x400")

Question = random.choice(questions)

Question_label = Label(window, text="Questions", font=("consolas", 30))
Question_label.pack(side="top", anchor=N, pady=20)

Asked_question = Label(window, text= Question,font=("consolas", 15))
Asked_question.pack(side="top", anchor=N, pady=20)

#----------------------------------------------------------------------------------
Next_button = Button(window, text="Next", font=("consolas", 20), command=Next)
Next_button.pack(side="top", anchor=S)

Restart_button = Button(window, text="Restart", font=("consolas", 15), command=Restart)
Restart_button.pack(side="top", anchor=S)

Close_button = Button(window, text="Close", font=("consolas", 10), command=window.destroy)
Close_button.pack(side="top", anchor=S)


# make a GUI for this question to make it easier
# repeat only 10 questions then move on to part 2, where you just gonna go and check other websites for the card. 
window.mainloop()