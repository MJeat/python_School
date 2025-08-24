    # Create rock paper scissors game: 

import random


    # Create rock paper scissors game: 

import random


def in_game():
    game = ["rock", 'paper', 'scissors']
    computer = random.choice(game)
    player = None
    while player not in game:
        player = input("Choose rock, paper, scissors: ").lower()


    print("computer: ", computer)
    print("Player: ", player)


    if (player == 'rock' and computer == 'paper') or \
    (player == "paper" and computer == 'rock') or \
    (player == "scissors" and computer == 'paper'): 
                print("Player Wins!")
    else: 
        print('Computer Wins!')    


def play_again():
    play_again= None
    options = ['yes','no']
    while play_again not in options:
        play_again = input('Play again?(yes/no):')


                
    
        if play_again != 'yes':
            print("GG")
            return False  # This line returns False, indicating that the player does not want to play again.
            
    
                
        else: 
            return True  # If the condition if play_again != 'yes': is not true, this line returns True, indicating that the player wants to play again.
        
while True:
    in_game()
    if not play_again(): # This line checks if the result of the play_again() function is False, which means the player does not want to play again.
        break  # If the condition if not play_again(): is true, this line breaks out of the loop, ending the game.
              
         
         
            
                
                


  
                
    

            
    


    
    


            
                
                


    
    

            
    


    
    

