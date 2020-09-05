from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://www.aalto.fi/en").text
soup = BeautifulSoup(source, "lxml")

articles = soup.find_all("div", class_="aalto-tile-container")

date = []
title = []
summary = []
for article in articles:
    try:
        date.append(article.find("span", class_="aalto-tile__meta-item aalto-tile__meta-item--label").text.strip())
        title.append(article.find("a", class_="aalto-tile__link").span.text.strip())
        summary.append(article.find("span", class_="aalto-tile__summary").text.strip())
    except:
        continue

final_array = []
for date, title, summary in zip(date, title, summary):
    final_array.append({"Date": date, "Title": title, "Summary": summary})

df = pd.DataFrame(final_array)

df.to_csv("aalto.csv")
    
