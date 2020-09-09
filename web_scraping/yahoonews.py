from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://hk.dictionary.search.yahoo.com/?_guc_consent_skip=1599639810").text
soup = BeautifulSoup(source, "lxml")

news_section = soup.find("div", class_="dd cardDesign sys_dict_news").ul

news = news_section.find_all("li")

title = []
source = []
time = []
description = []
link = []
for new in news:
    title.append(new.h4.a.text)
    link.append(new.h4.a.get("href"))
    source.append(new.span.text)
    time.append(new.find_all("span")[1].text)
    description.append(new.p.text)

final_array = []
for title, link, source, time, description in zip(title, link, source, time, description):
    final_array.append({"Title": title, "Link": link, "Source": source, "Time": time, "Description": description})

df = pd.DataFrame(final_array)

df.to_csv("yahoo_news.csv")