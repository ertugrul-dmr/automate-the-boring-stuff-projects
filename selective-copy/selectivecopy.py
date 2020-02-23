# program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
import shutil
import os

# Find the paths and assign them to variables.
inputPath = os.path.abspath('input folder path')
outputPath = os.path.abspath('output folderpath')
# Make list of input dir.
listFiles = os.listdir(inputPath)


# Go through the os.listdir and find specific file types.

def searcher(minput):
    fileExtensions = []
    y = minput
    fileExtensions.append(y)
    fileExtensions = tuple(fileExtensions)
    fileMatches = [file for file in listFiles if file.endswith(fileExtensions)]

    # Use shutil copy for each file.
    for i in range(len(fileMatches)):
        shutil.move(
            f'{inputPath}//{fileMatches[i]}', f'{outputPath}//{fileMatches[i]}')
        print(f'Moving {fileMatches[i]} to {outputPath}')
    print(f'Done!\n{len(fileMatches)} files succesfully moved!')


while True:
    yn = input(f'Do you wanna move files {inputPath} to {outputPath} (Y/N): ')
    yn.lower()
    if yn == 'y':
        searcher(input('Please enter file extension with a dot(like .txt): '))

    else:
        break
