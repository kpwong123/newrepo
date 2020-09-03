from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://www.tokyo-koryaku.com/").text
soup = BeautifulSoup(source, "lxml")

blocks = soup.find("div", class_="equalFourCol01 indexCol01 equalHeight explanCol").find_all("div")

info = []
for block in blocks:
    try:
        row = []
        category = block.find("div", class_="infoBlock").p.text
        title = block.find("p", class_="equalChildTxt").text
        date = block.find("p", class_="date").text
        caption = block.find("p", class_="explanTxt").text
        row.append(category)
        row.append(title) 
        row.append(date)
        row.append(caption)
        info.append(row)
    except:
        continue
    #unexpected nonetype error occured, solved by try/except without explanation. required deeper understanding

with open("japan_info.csv", "w", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(info)