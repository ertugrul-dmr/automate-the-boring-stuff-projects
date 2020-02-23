# Debugged the basic coin toss...
import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    guess.lower()
    logging.debug(f'You entered {guess}')
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug(f'{toss} came up')
if toss == 0:
    toss = 'heads'
if toss == 1:
    toss = 'tails'
if guess == toss:
    logging.debug(f'Your guess was {guess} and toss was {toss}')
    print('You got it!')
else:
    print('Nope! Guess again!')
    logging.debug(f'Your guess was {guess} and toss was {toss}')
    guess = input()
    if toss == guess:
        logging.debug(f'Your guess was {guess} and toss was {toss}')
        print('You got it!')
    else:
        logging.debug(f'Your guess was {guess} and toss was {toss}')
        print('Nope. You are really bad at this game.')
