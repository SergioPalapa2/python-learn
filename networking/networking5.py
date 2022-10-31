#webscraping
#Software libreria beautiful soup. Provee una libreria para realizar analisis y webscraping de forma mas facil
#apt-get install python3-bs4  //instalacion
#pip install beautifulsoup4  //instalacion mediante pip

import urllib.request
from bs4 import BeautifulSoup

url=input('Enter - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

#Regresa todos los tags
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))