# A program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.

import os
import re
# Set working directory or set path
inputPath = os.path.abspath('path to input folder')

folderContent = os.listdir(inputPath)
folderContent.sort()
# Use regex to find patterns
print(folderContent)
stringofFiles = str(folderContent)

fileRegex = re.compile(r'''(
    (\w+)
    (\d{3})
    (\.txt)
    )''', re.VERBOSE)

fileMatches = fileRegex.findall(stringofFiles)

number = 1
fileNames = []
for groups in fileMatches:
    fileName = ''.join([groups[1], str(number).zfill(3), groups[3]])
    fileNames.append(fileName)
    number += 1

# Use os to rename files

for i in range(len(fileNames)):
    src = os.path.join(inputPath, folderContent[i])
    out = os.path.join(inputPath, fileNames[i])
    os.rename(src, out)
