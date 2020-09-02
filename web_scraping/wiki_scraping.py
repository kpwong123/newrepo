from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

source = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population").text
soup = BeautifulSoup(source, "lxml")

table = soup.find("table", class_ = 'wikitable sortable')

#jquery-tablesorter is not included

country_rows = table.find_all("tr")

for country_row in country_rows:
    try:
        country_cell = country_row.find_all("td")[0]
        country_link = country_cell.find_all("a")[0].get('href')
        print(country_link)
    except:
        countrycell = None

