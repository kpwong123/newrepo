from bs4 import BeautifulSoup
import requests
import csv
import numpy as np

source = requests.get("http://totaljerkface.com/").text
soup = BeautifulSoup(source, "lxml")

sections = soup.find_all("div", class_="section")

article_array = []
for section in sections:
    title = section.find("span", class_="title").string
    body = section.find("div", class_="news_item_body").find("div", class_="news_item_body").text
    article_list = [title, body]
    article_array.append(article_list)
print(article_array)

#encoding="utf-8" is added argument of the open method orelse if will raise an error
with open("wheels.csv", "w", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(article_array)
