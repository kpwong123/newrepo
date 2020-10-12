from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://mall.jetour.com.hk/%E7%B6%B2%E4%B8%8A-online-wine_cellar-%E8%91%A1%E8%90%84%E9%85%92-wine-%E7%94%9C%E9%85%92").text

soup = BeautifulSoup(source, "lxml")

section = soup.find("div", class_="master-column-wrapper").find("div", class_="page category-page").find("div", class_="item-grid")

titles = []
prices = []
urls = []
for item in section.find_all("div", class_="item-box"):
    titles.append(item.find("h2", class_="product-title").a.text)
    prices.append(item.find("span", class_="price actual-price").text)
    urls.append(item.find("h2", class_="product-title").a.get("href"))

print(prices)

countries =[]
types = []
volumes = []
for url in urls:
    ind_source = requests.get("https://mall.jetour.com.hk" + url).text
    ind_soup = BeautifulSoup(ind_source, "lxml")
    info = ind_soup.find("div", class_="short-description").text
    temp1 = info.split("國家：")
    temp2 = temp1[1].split("地區：")
    countries.append(temp2[0].strip())
    temp3 = temp2[1].split("酒類：")
    temp4 = temp3[1].split("容量：")
    types.append(temp4[0].strip())
    temp5 = temp4[1].split("評分：")
    volumes.append(temp5[0].strip())

final_array = []
for name, price, country, wine_type, volume in zip(titles, prices, countries, types, volumes):
    final_array.append({"Name": name, "Price": price, "Origin": country, "Type": wine_type, "Volume": volume})

df = pd.DataFrame(final_array)

df.to_csv("wine.csv")