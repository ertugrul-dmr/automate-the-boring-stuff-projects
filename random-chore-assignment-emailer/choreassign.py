import random
import smtplib
# Get a list of ppl mail adresses and list of chores.
chores = ['chore1', 'chore2', 'chore3', 'chore4']
mails = ['mail1', 'mail2', 'mail3', 'mail4']

# Use for loop in range of list of chores.
for i in range(len(chores)):
    # Use random.choice to select chores and assign them to random email. Use .remove to remove from lists
    randomChore = random.choice(chores)
    randomMail = random.choice(mails)
    # Use smtplib to send mails
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)  # smtp adress
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('example@example.com', 'example_password')
    smtpObj.sendmail('example@example.com',
                     f'{randomMail}', f'\n{randomChore}: this is your daily chore.')
    chores.remove(randomChore)
    mails.remove(randomMail)
    with open('past_chores.txt', 'a') as file:
        file.write(f'{randomChore} > {randomMail}\n')
    if len(chores) == 0:
        with open('past_chores.txt', 'a') as file:
            file.write(f'Week ends!\n')
smtpObj.quit
