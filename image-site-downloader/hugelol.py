# A program that goes to hugelol, and then downloads all the resulting images.
from bs4 import BeautifulSoup
import requests
import os
os.makedirs('test', exist_ok=True)
source = requests.get('https://hugelol.com/')
src = source.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for pic in soup.find_all("div", {"class": "source"}):
    for a in pic.find_all('img'):
        urls.append(a['src'])
for i in urls:
    url = f'{i}'
    res = requests.get(url)
    imageFile = open(os.path.join('memes', os.path.basename(url)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
