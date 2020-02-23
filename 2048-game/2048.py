# A program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes to automatically play the game.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import random
import time

sys.setrecursionlimit(10000)
driver = webdriver.Firefox()
driver.get('https://play2048.co/')
time.sleep(1)


game = driver.find_element_by_xpath('/html/body')


def x():
    while True:
        moves = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
        y = random.choice(moves)
        game.send_keys(y)
        y = random.choice(moves)
        game.send_keys(y)
        y = random.choice(moves)
        game.send_keys(y)
        y = random.choice(moves)
        y = random.choice(moves)
        game.send_keys(y)
        try:
            driver.find_element_by_partial_link_text("Try again")
            driver.find_element_by_partial_link_text("New Game").click()
        except:
            x()


x()
