User
import requests
from bs4 import BeautifulSoup
import schedule
import time

url = "https://replit.com/community-hub"

reponse = requests.get(url)
html = reponse.text

soup = BeautifulSoup(html, 'html.parser')

#<div class="css-hakv9k">flexscroll-snap
#<div class="css-1qpntov">flex

myLink = soup.find_all('div', {"class" : "css-1qpntov"})
link = myLink.text("a")
counter = 0

for link in myLink:
  print(link.text)
  thisLink = link.find('a')['href']
  print(thisLink)

counter += 1