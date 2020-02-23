import os
sizeFile = open(f'filesizes.txt', 'w')
# Determine input path location and assign a value to it.
inputDirectory = os.path.abspath('path to folder')
# Use walkfolder to go through every subfolder and files.
for folderName, subfolders, filenames in os.walk(inputDirectory):
    print(f'-----' * 50)
    print(f'The current folder is {folderName}')
    sizeFile.write(f'The current folder is {folderName}\n')
    print(f'-----' * 50)
# Use os.path.getsize() to get files more than 100mb and print these with their absolute path.
    for filename in filenames:
        path = os.path.join(folderName, filename)
        size = os.path.getsize(path)
        if size > 100 * 2**20:
            sizeFile.write(f'{int(size/2**20)}MB, {filename}, {path}\n')
            print(f'{int(size/2**20)}MB, {filename}, {path}')
sizeFile.close()
input()
