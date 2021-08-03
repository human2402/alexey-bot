from bs4 import BeautifulSoup
import requests
from random import randrange

def getCongrat():
    randomPage = randrange(1,10)
    htmlText = requests.get('https://pozdravok.ru/pozdravleniya/lyubov/spokoynoy-nochi/'+str(randomPage)).text
    soup = BeautifulSoup(htmlText, 'lxml')
    grettings = soup.find('p', class_ = "sfst")
    newGreet = ""
    for line in grettings:
        if line != "<br/>":
            newGreet += str(line) + '\n'
    print(newGreet)

getCongrat()