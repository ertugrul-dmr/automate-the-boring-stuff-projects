# This is a game tries to simulate rock, paper, scissors game.
import random
import sys


def maingame():  # Start's the game if player chooses to play.
    wins = 0
    losses = 0
    draws = 0

    while True:  # Main loop
        print(f'Wins: {wins}, Losses: {losses}, Draws: {draws}')
        if wins == 5:
            print(f'You beat the ai!')
            break
        if losses == 5:
            print(f'Ai has beaten you!')
            break
        if draws == 5:
            print(f'It\'s a draw between you and ai!')
            break

        playerMove = str(
            input('Plese make your move. r(ock),p(aper),s(scissors): '))
        aiMove = random.randint(1, 3)  # 1 rock, 2 paper, 3 scissor
        if playerMove == 'r':
            if aiMove == 1:
                print('Ai move is: Rock.' + f' Your move was: {playerMove}.')
                print('Draw')
                draws += 1
            elif aiMove == 2:
                print('Ai move is: Paper.' + f' Your move was: {playerMove}.')
                print('Lose')
                losses += 1
            else:
                print('Ai move is: Scissor.' +
                      f' Your move was: {playerMove}.')
                print('Win')
                wins += 1
        if playerMove == 'p':
            if aiMove == 2:
                print('Ai move is: Paper.' + f' Your move was: {playerMove}.')
                print('Draw')
                draws += 1
            elif aiMove == 3:
                print('Ai move is: Scissor.' +
                      f' Your move was: {playerMove}.')
                print('Lose')
                losses += 1
            else:
                print('Ai move is: Rock.' + f' Your move was: {playerMove}.')
                print('Win')
                wins += 1
        if playerMove == 's':
            if aiMove == 3:
                print('Ai move is: Scissor.' +
                      f' Your move was: {playerMove}.')
                print('Draw')
                draws += 1
            elif aiMove == 1:
                print('Ai move is: Rock.' + f' Your move was: {playerMove}.')
                print('Lose')
                losses += 1
            else:
                print('Ai move is: Paper.' + f' Your move was: {playerMove}.')
                print('Win')
                wins += 1
    k = input(f'Enter R to restart and press Q to quit\nR/Q? ')
    k.lower()
    if k == 'r':
        maingame()
    else:
        sys.exit


k = input(f'Enter S to restart and press Q to quit\nS/Q? ')
k.lower()
if k == 's':
    maingame()
else:
    sys.exit
