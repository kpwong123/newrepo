from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://www.cwchu.cuhk.edu.hk/en-gb/learning-and-teaching/college-general-educational-program/non-credit-bearing-courses/course-description").text

soup = BeautifulSoup(source, "lxml")

items = soup.find("div", class_="item-page")
tables = items.tr.td.find_all("div")[2].find_all("table")

for table in tables:
    rows = table.find_all("tr")

    fraction = []
    for row in rows:
        cells = row.find_all("td")
        table_row = []
        for cell in cells:
            table_row.append(cell.text.strip())
        fraction.append(table_row)

    with open("gecw.csv", "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(fraction)