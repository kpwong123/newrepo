from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://www.parknshop.com/zh-hk/").text

soup = BeautifulSoup(source, "lxml")

container = soup.find("div", class_="product-container swiper-wrapper")

items = container.find_all("div", recursive=False)

names = []
prices = []
urls = []
for item in items:
    names.append(item.find("div", class_="name").a.p.text.strip())
    prices.append(item.find("div", class_="price discount newPrice").text)
    urls.append(item.find("div", class_="name").a.get("href"))

codes = []
for url in urls:
    ind_source = requests.get("https://www.parknshop.com" + url).text
    ind_soup = BeautifulSoup(ind_source, "lxml")
    try:
        codes.append(ind_soup.find("span", class_="productvariantCode").text)
    except:
        codes.append("error")

finalarray = []
for name, price, code in zip(names, prices, codes):
    finalarray.append({"Name of Product": name, "Price": price, "Product Code": code})

df = pd.DataFrame(finalarray)

df.to_csv("parknshop.csv")