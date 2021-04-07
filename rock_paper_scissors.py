'''
Created on Mar 6, 2021

Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner)

Remember the rules:

Rock beats scissors
Scissors beats Paper
Paper beats Rock

@author: lindseymerwin
'''

        

    


def rock_paper_scissors():
# each player selects their first move
    player1 = input('Player 1 enter first move: ')
    player2 = input('Player 2 Enter first move: ')
    
    if player1 and player2 in moves:
        
        player1 = moves[player1]
        player2 = moves[player2]

        if player1 == 1:
            if player2 == 3:
                print('PLAYER 1 WINS!')
        
            elif player2 == 2:
                print('PLAYER 2 WINS')
        
            elif player2 == 1:
                print('CATS GAME')  
        
        if player1 == 2:
            if player2 == 1:
                print('PLAYER 1 WINS!')
        
            elif player2 == 3:
                print('PLAYER 2 WINS')
        
            elif player2 == 2:
                print('CATS GAME') 
                
        if player1 == 3:
            if player2 == 2:
                print('PLAYER 1 WINS!')
        
            elif player2 == 1:
                print('PLAYER 2 WINS')
        
            elif player2 == 3:
                print('CATS GAME') 
        
    else:
        print('Invalid, must be rock, paper, or scissors')



moves = {'rock': 1, 'paper': 2, 'scissors': 3} # <-- gives options
user_moves = rock_paper_scissors()


