import requests
import bs4
import smtplib

# use requests and bf4 to find if its raining

res = requests.get(
    'https://weather.com/weather/today/l/33d1e415eb66f3e1ab35c3add45fccf4512715d329edbd91c806a6957e123b49')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
condition = soup.find("div", {"class": "today-daypart-top"}).text

# if its raining then send a mail to user.
if 'rain' not in condition.lower():
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('fbhce1@outlook.com', 'Alex*10*')
    subject = 'WARNING'
    msg = f'subject:{subject}\n\nIt\'s raining today, yoy better bring yout umbrella with you!'
    smtpObj.sendmail('fbhce1@outlook.com', 'podowski@yahoo.com', msg)
    smtpObj.quit
