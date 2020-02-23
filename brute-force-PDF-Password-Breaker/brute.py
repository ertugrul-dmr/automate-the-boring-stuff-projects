# A program that will decrypt the PDF by trying every possible English word until it finds one that works.
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('yourpdfname.pdf', 'rb'))

with open('dictionary.txt', 'r') as dictionary:
    dicts = dictionary.read().splitlines()


for dic in dicts:
    if pdfReader.decrypt(f'{dic.lower()}') == 1:
        print(f'The password is: {dic.lower()}')
        break
    elif pdfReader.decrypt(f'{dic}') == 1:
        print(f'The password is: {dic.lower()}')
        break
    else:
        print(f'{dic.lower()} and {dic} FAILED')
