import random
import time


#-----------------------------------------------------------------------
while True:

    game = ['rock', 'paper','scissors']

    computers = random.choice(game)



    player = None
    while player not in game:
        player = input('Choose rock, paper, scissors: ').lower()

    print('player: ', player)
    print('computer: ', computers)


    if (player == 'rock' and computers == 'scissors') or \
    (player == 'paper' and computers == 'rock') or \
    (player == 'scissors' and computers == 'paper'):
        print("player wins!")

    else:
        print('computer wins!')



    while True:
        player_options = input('Play again? The chance of getting out is 50/50 (yes/no): ').lower()
        options = ['yes', 'no']
        computer_options = ['Nah, I am tired', 'You Are Not Going Anywhere!!']
        chance_getting_out= random.choice(computer_options)


        if player_options in options:
            for i in range(1, 0, ):
                time.sleep(1)
                print(i)
            print('Choosing for you...')
        
            for j in range(3, 0, -1):
                    print(j)
                    time.sleep(1)

            print('Computer Response: ', chance_getting_out)
            break
        

    if chance_getting_out == 'Nah, I am tired':
        
        print('You are Lucky. See You Next Time!')
        break
    else:
        
        print('Rematch!')
    
#-----------------------------------------------------------------------