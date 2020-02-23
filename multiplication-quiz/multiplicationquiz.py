# multiplicationquiz.py
# This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9.
# If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
# The user gets three tries to enter the correct answer before the program moves on to the next question.
# Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.

import random
import time
import pyinputplus as pyip

numberOfQuestions = 10
correctAnswers = 0

for question in range(numberOfQuestions):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    try:
        # Creates random multiplication question.
        print(f'{question+1}# {x} * {y} = ?')
        response = pyip.inputNum(allowRegexes=['^%s$' % (x * y)],
                                 blockRegexes=[('.*', 'Incorrect!')],
                                 timeout=8, limit=3)

    except pyip.TimeoutException:
        print('Out of time!')
        time.sleep(1)
    except pyip.RetryLimitException:
        print('Out of tries!')
        time.sleep(1)
    else:
        print('Correct!')
        correctAnswers += 1
        time.sleep(1)
correctcount = f'Out of {numberOfQuestions} you answered %s of it' % (
    correctAnswers)
print(correctcount)
