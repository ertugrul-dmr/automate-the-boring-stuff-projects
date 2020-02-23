# Automate the Boring Stuff With Python Ch. 4 Project

spam = ['apples', 'bananas', 'tofu', 'cats', 'coconuts']


def commacode(spam):  # Combines list into a string of the form item1, item2, item 3 and item 4
    for i in spam:
        if i == spam[len(spam) - 1]:
            print(f'and {i}')
        elif i == spam[len(spam) - 2]:
            print(i, end=' ')

        else:
            print(f'{i} , ', end='')


commacode(spam)
