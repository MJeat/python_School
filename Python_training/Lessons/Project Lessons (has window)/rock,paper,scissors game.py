import random 

while True:

    game = ['rock', 'paper','scissors']
    computer = random.choice(game)

    player_input = None
    while player_input not in game:
        player_input = input('Choose rock, paper or scissors: ').lower()





    print("player_input: "+ player_input)
    print("Computer: " + computer)


    if player_input == computer:
        print('A Tie!')

    elif (player_input == 'rock' and computer == 'scissors') or \
        (player_input == 'paper' and computer == 'rock') or \
        (player_input == 'scissors' and computer == 'paper'):
        print("Player Wins!")


    else:
        print('Computer Wins! ')


    while True: 
        player_options = input('Want To Continue? (yes/no): ').lower()

        options = ['yes', 'no']

        if player_options in options:
            break

    if player_options == 'no':
        print("Come Again Next Time!")
        break


    


    
    