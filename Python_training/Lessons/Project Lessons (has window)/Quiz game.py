def new_game():


    player_list = []
    correct_guess = 0



    
    for question, answer in questions.items():#so if i use only questions():, then I will only get the key and not the values
        print('----------------------')
        print(question)

        for option in options[question]: # options[question] is to call the value from options to question that is from the questions      
            print(option)
            
        

        player = input('Choose A,B,C: ').upper()
        while player not in ['A','B','C']:
            player = input('Choose A,B,C: ').upper()

        player_list.append(player) #it adds the value in the guess list to the guesses list (above)


        if player == answer:
            print('CORRECT')
            correct_guess += 1

        else:
            print('WRONG')


        score(correct_guess, player_list)

        
def score(correct_guess, player_list):
    print('----------------------')
    print('Result:')
    print("Player guesses: ", *player_list)
    print('Answer',*questions.values())  #Put star * in order to display the answer nicely. If remove, it will give the ugly box
    print("Your score is: ", int(correct_guess/len(questions)*100), '%')



def play_again():
    while True: 
        play_again = input('Play Again? (yes/no): ').lower()
        while play_again not in ['yes', 'no']:
            print('Please enter yes or no.')  # This would create an infinite loop
            play_again = input('Play Again? (yes/no): ').lower()
        return play_again == 'yes'





questions = {'What is love?': 'A',
             'What 2+2?': 'B',
             'Choose one': 'C'
             
        }



options = {'What is love?':['A. Coconut','B. Ice cream', 'C. Cat'],
           'What 2+2?':['A. 4','B. 5','C. 6'],
           'Choose one':['A. True','B. False','C. one']
           }

new_game()


while play_again():
    new_game()

print('GG')

#Next task is to start while loop from the beginning