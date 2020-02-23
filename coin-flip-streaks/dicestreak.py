# My alternative version of Coin Flip Streaks, used dice instead of it.

# Write a program to find out how often a streak of six numbers comes up in a randomly generated list of dices.
import random
numberOfStreaks = 0
# Code that creates a list of 100 dice values.
for experimentNumber in range(10000):
    results = []
    for experiment in range(100):
        x = random.randint(1, 6)
        if x == 1:
            results.append('1')
        elif x == 2:
            results.append('2')
        elif x == 3:
            results.append('3')
        elif x == 4:
            results.append('4')
        elif x == 5:
            results.append('5')
        elif x == 6:
            results.append('6')
# Code that checks if there is a streak of 6 same numbers in a row.
    currentStreak = 0
    previousResult = results[0]

    for result in results:
        if currentStreak == 6:
            numberOfStreaks += 1
            currentStreak = 0
        if result == previousResult:
            currentStreak += 1
        previousResult = result

print('Sum of expected values multiplied by their respective probability: %s%%' %
      (numberOfStreaks / 100))
