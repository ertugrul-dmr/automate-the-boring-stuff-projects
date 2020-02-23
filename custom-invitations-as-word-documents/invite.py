# A program that would generate a Word document with custom invitations
import docx
# Document with the custom style saved:
doc = docx.Document('New Microsoft Word Document.docx')

with open('guests.txt') as file:
    guests = file.readlines()

for guest in guests:
    print(guests)
    doc.add_paragraph(f'''
        It would be a pleasure to have the company of
        {guest}
        at 1010 Memory Lane on the Evening of
        April 1st
        at 7 o'clock''', style='pyth1')  # This style created on word, can't be used on other word files, need to create new one...
    doc.add_page_break()
doc.save('new.docx')
