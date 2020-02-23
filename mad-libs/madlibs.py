# madlibs.py
# A program that asks user for some inputs and gives mad lib output.
# Will add regex to find adj, noun and verbs...

madLibfile = open('madlibOutput.txt', 'w')

adjective = input(f'Enter an adjective: ')
noun = input(f'Enter a noun: ')
noun1 = input(f'Enter a noun: ')
verb = input(f'Enter a verb: ')
noun2 = input(f'Enter a noun: ')

madLibfile.write(
    f'The {adjective} panda walked to the {noun} and then {noun1}. A nearby {noun2} was unaffected by these events.')

madLibfile.close()

madLibfile = open('madlibOutput.txt', 'r')
y = madLibfile.read()
print(y)
madLibfile.close()
input()
