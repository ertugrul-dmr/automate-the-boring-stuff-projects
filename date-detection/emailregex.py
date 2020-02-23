#emailregex.py
#email version of Date Detection

import re

#random mail adresses:
mails = '''syrinx@aol.com
    adsfasdfgv@zmge.wheee
    gumpish@msn.com
    ramollin@hotmail.com
    joelw@yahoo.com
    noticias@yahoo.ca
    osaru@live.com
    luebke@aol.com
    barjam@icloud.com
    jigsaw@optonline.net
    giafly@me.com
    choset@outlook.com
    alfred@optonline.net'''

emailRegex = re.compile(r'''(
    ([a-zA-Z0-9._%+-]+)     # username
    (@)                      # @ symbol
    ([a-zA-Z0-9.-]+)         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

matches = []

for groups in emailRegex.findall(mails):
    mail = ''.join([groups[1], groups[2], groups[3], groups[4]])
    matches.append(mail)

for i in matches:
    print(i, end='\n')
