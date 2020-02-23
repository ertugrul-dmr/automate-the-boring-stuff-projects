# sandwich.py
# A program that asks users for their sandwich preferences.
import pyinputplus as pyip


def sandwich():
    # I assigned these prices completely random :)
    prices = {'Wheat': 2, 'White': 2.50, 'Sourdough': 3, 'Chicken': 2, 'Turkey': 2,
              'Ham': 3, 'Tofu': 3, 'Cheddar': 1, 'Swiss': 2, 'Mozzarella': 1.50, 'saucey': 0.50}

    print(f'To select bread type:')
    bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
    print(f'To select protein type:')
    protein = pyip.inputMenu(
        ['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)

    cheese = pyip.inputYesNo(
        'Do you want cheese? Please enter yes if you do, and no if you don\'t: ')

    if cheese.lower() == 'yes':
        print('To select cheese type:')
        cheesetype = pyip.inputMenu(
            ['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
    if cheese.lower() == 'no':
        cheesetype = 'Cheddar'
        prices['Cheddar'] = 0

    sauce = pyip.inputYesNo(
        'Do you want mayo, mustard, lettuce, or tomato in sandwich?: ')
    if sauce.lower() == 'yes':
        sauce = 'saucey'
    if sauce.lower() == 'no':
        sauce = 'saucey'
        prices['saucey'] = 0

    each = pyip.inputInt('How many sandwiches you want: ', min=1)
    if cheese.lower() == 'yes':
        print(f'You choose {bread},{protein},cheese:{cheese}', f'({cheesetype}), ',
              f'Sauce:{sauce}, {each} sandwiches.')
    if cheese.lower() == 'no':
        print(f'You choose {bread},{protein},cheese:{cheese}',
              f'Sauce:{sauce}, {each} sandwiches.')
    y = pyip.inputYesNo('You want to buy? (Yes/No) ')
    if y == 'yes':
        print((prices.get(str(bread)) + prices.get(str(protein)) +
               prices.get(str(cheesetype)) + prices.get(str(sauce))) * int(each))
    if y == 'no':
        sandwich()


while True:
    print('Would you like to have a sandwich? (Yes/No): ')
    x = pyip.inputYesNo()
    if x.lower() == 'yes':
        sandwich()
    else:
        print('If you say so...')
        break
