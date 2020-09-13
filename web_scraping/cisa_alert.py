from bs4 import BeautifulSoup
import requests
import pandas as pd

year_list = []
number_list = []
title_list = []

for year in range(2004,2008):
    source = requests.get("https://us-cert.cisa.gov/ncas/archives/alerts/" + str(year)).text
    soup = BeautifulSoup(source, "lxml")

    alerts = soup.find("div", class_="item-list").find_all("li")

    for alert in alerts:
        number = alert.text.split(":")[0].strip()
        title = alert.text.split(":")[1].strip()
        number_list.append(number)
        title_list.append(title)
        year_list.append(year)

for year in range(2008,2021):
    source = requests.get("https://us-cert.cisa.gov/ncas/alerts/" + str(year)).text
    soup = BeautifulSoup(source, "lxml")

    alerts = soup.find("div", class_="item-list").find_all("li")

    for alert in alerts:
        number = alert.text.split(":")[0]
        title = alert.text.split(":")[1].strip()
        if "\n" in number:
            amended_number = number.replace("\n", "")
            number_list.append(amended_number)
        else:
            number_list.append(number)
        title_list.append(title)
        year_list.append(year)

print(number_list)


final_array = []
for year, number, title in zip(year_list, number_list, title_list):
    final_array.append({"Year of Alert": year, "Code": number, "Title of Alert": title})

df = pd.DataFrame(final_array)

df.to_csv("cisa_alert.csv")