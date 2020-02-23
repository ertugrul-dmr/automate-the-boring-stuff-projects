# Checks user given password for at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.

import re


def checker(password):
    if passRegex.search(password) == None:
        return False
    else:
        return True


passRegex = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).(?=.*\W){8,}')

while True:  # Asks until strong password is given. Will update it so it prints whats missing too...
    enter = input(f'Please enter a password to be checked.\nNeeds to contain at least an uppercase and lowercase letter, a symbol and a number.\nAnd must be least 8 characters long: ')
    if checker(enter) == True:
        print("Strong Password")
        break
    else:
        print("This is not a strong password")
