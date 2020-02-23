#My approach to the Coin Flip Streaks practice

#Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.



import random
numberOfStreaks = 0
# Code that creates a list of 100 'heads' or 'tails' values.
for experimentNumber in range(10000):
    results = []
    for experiment in range(100):
        x = random.randint(1, 2)  # 1 for heads and 2 for tails
        if x == 1:
            results.append('H')
        else:
            results.append('T')
# Code that checks if there is a streak of 6 heads or tails in a row.
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
