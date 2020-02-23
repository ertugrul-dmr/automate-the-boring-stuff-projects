# A program to read in the contents of several text files
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

text = open('text.txt', 'r')
lines = text.readlines()

for i in range(len(lines)):
    sheet.cell(row=i + 1, column=1).value = lines[i]
wb.save('spread.xlsx')
