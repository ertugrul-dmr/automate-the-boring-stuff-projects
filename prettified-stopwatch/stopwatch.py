#! python3
# stopwatch.py - A simple stopwatch program.

import time
import pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1
copy = ''

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        laps = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(
            totalTime).center(7), str(lapTime).rjust(6))
        print(laps, end='')
        copy += laps + '\n'
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    pyperclip.copy(copy)
    print('\nDone.')
