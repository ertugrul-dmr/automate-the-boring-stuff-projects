#My another approach to the slective copy practice without regex.

import os
import shutil
# Find the paths and assign them to variables.
inputPath = os.path.abspath('input path')
outputPath = os.path.abspath('output path')
# Use os.walk to go through folder.
for root, dirs, files in os.walk(inputPath):
    for file in files:
        path = os.path.join(root, file)
        print(file)
        # Use shutil to move them
        if file.endswith('.jpg'):
            shutil.copy(path, outputPath)

#This one walks through subfolders too and I didn't fixed it yet.
