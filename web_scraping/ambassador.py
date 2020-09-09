from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://lces.osa.cuhk.edu.hk/the-i-ambassador-scheme-2020-21/").text
soup = BeautifulSoup(source, "lxml")

mytable = soup.find_all("table")[0].table

date = []
event = []
for row in mytable.find_all("tr"):
    date.append(row.find_all("td")[0].text)
    temp = row.find_all("td")[1].text
    temporary = temp.replace("\n", "")
    event.append(temporary)
print(date)
print(event)

final_array = []
for date, event in zip(date, event):
    final_array.append({"Date": date, "Events": event})

df = pd.DataFrame(final_array)

df.to_csv("ambassador.csv")
