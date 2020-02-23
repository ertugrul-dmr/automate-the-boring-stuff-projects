
# Another variation to automate the Boring Stuff With Python Ch. 4 Project
spam = ['apples', 'bananas', 'tofu', 'cats', 'coconuts']


def comma(items):  # Combines list into a string of the form item1, item2, item 3 and item 4
    if len(items) == 1:
        print(items[0])
    print('{} and {}'.format(', '.join(items[:-1]), items[-1]))


comma(spam)
