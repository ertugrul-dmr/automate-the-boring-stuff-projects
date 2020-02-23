# A program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.
import re
import os
from pathlib import Path

datadir = Path('your path here')

files = os.listdir(datadir)

textRegex = re.compile(r'.*\.txt')
fileMatches = list(filter(textRegex.match, files))

search = input(f'''Please enter what you are trying to find in
    {datadir} txt files: ''')

for i in range(len(fileMatches)):
    madlibFile = open(f'{datadir}\\{fileMatches[i]}')
    readed = madlibFile.read()
    innerRegex = re.compile(f'{search}', re.IGNORECASE)
    matches = innerRegex.findall(readed)
    for match in matches:
        if match != []:
            print(f'{matches} in {datadir}/{fileMatches[i]}')
