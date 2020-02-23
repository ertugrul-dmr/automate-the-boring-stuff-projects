# dateregex.py
# Finds and prints date formats from the given string.
import re

dates = ''' your text goes here for search'''

dateRegex = re.compile(r'''(
    (\d{2}) #DD
    (\-|\.) #- or .
    (\d{2}) #MM
    (\-|\.) #- or .
    (\d{4}) #Year
    )''', re.VERBOSE)


matches = []

for groups in dateRegex.findall(dates):
    date = '-'.join([groups[1], groups[3], groups[5]])
    # Some months can't be 31 days
    if groups[3] == ('04' or '06' or '09' or '11') and int(groups[1]) > 30:
        print(f'Error invalid date: {date}')
    # February exceptions
    if groups[3] == '02' and int(groups[1]) > 28 and int(groups[5]) % 4 != 0:
        print(f'Error invalid date: {date}')
    else:
        date = '-'.join([groups[1], groups[3], groups[5]])
        matches.append(date)


for i in matches:
    print(i, end='\n')
