from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population").text
soup = BeautifulSoup(source, "lxml")

table = soup.find("table", class_="wikitable sortable")


country_name = []
country_link = []
country_population = []
country_percentage = []
for row in table.tbody.find_all("tr")[1:]:
    try:
        country_name.append(row.td.a.text)
        country_link.append(row.td.a.get("href"))
        country_population.append(row.find_all("td")[1].text)
        country_percentage.append(row.find_all("td")[2].text)
    except:
        pass
print(country_name)
print(country_population)
print(country_percentage)

temp_country_link = []
for link in country_link:
    temp_country_link.append(link.replace("Demographics_of_", ""))
country_link = temp_country_link
print(country_link)

area =[]
water_percentage = []
counter = 0
for country in country_link:
    country_source = requests.get("https://en.wikipedia.org" + country).text
    country_soup = BeautifulSoup(country_source, "lxml")
    infobox = country_soup.find("table", class_="infobox geography vcard")
    read_area = False
    read_water = False
    try:
        for info_row in infobox.find_all("tr"):
            try:
                if info_row.th.text == "Area " or info_row.th.text == "Area":
                    try:
                        utext = info_row.next_sibling.td.text
                        utextlist = utext.split()
                        utextlist2 = utextlist[0].split("[")
                        area.append(utextlist2[0])
                        read_area = True
                    except:
                        pass
                    try:
                        uwater = info_row.next_sibling.next_sibling.td.text
                        uwaterlist = uwater.split("[")
                        uwaterlist2 = uwaterlist[0].split()
                        water_percentage.append(uwaterlist[0])
                        read_water = True
                    except:
                        pass
                    # print(area)
                    # print(water_percentage)
                else:
                    pass
            except:
                pass
    except:
        pass
    if read_area == True:
        pass
    elif read_area == False:
        area.append("(No Info)")
    if read_water == True:
        pass
    elif read_water == False:
        water_percentage.append("(No info)")
    counter += 1
    print("Progress: " + str(counter) + " out of 241 countries")
print(len(area), len(water_percentage))

final_array = []
for name, population, percentage, area, water in zip(country_name, country_population, country_percentage, area, water_percentage):
    final_array.append({"Name of Country":name, "Population":population, "Population %":percentage, "Total Area":area + " km2", "Water Area %":water + "%"})
df = pd.DataFrame(final_array)
df.to_csv("country.csv")