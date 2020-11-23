from bs4 import BeautifulSoup
import pandas as pd
import requests

source = requests.get("https://www.bbc.com/weather/1819729").text

soup = BeautifulSoup(source, "lxml")

items = soup.find("div", class_="wr-time-slot-list__item wr-time-slot-list__item--time-slots").find_all("li", class_="wr-time-slot wr-js-time-slot")

for item in items:
    ctemps.append(item.find("span", class_="wr-value--temperature--c").text)

ftemps = []
for x in ctemps:
    y = x.replace("°", "")
    ftemps.append(int(y) * 9 / 5 + 32)

