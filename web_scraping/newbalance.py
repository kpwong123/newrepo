from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://www.ebay.com/str/joesnewbalanceoutlet").text

soup = BeautifulSoup(source, "lxml")

menu = soup.find("ul", class_="b-list__items_nofooter srp-results srp-grid")

items = menu.find_all("li", class_="s-item")

names = []
prices = []
urls = []
for item in items:
    names.append(item.find("div", class_="s-item__info clearfix").a.text)
    prices.append(item.find("div", class_="s-item__detail s-item__detail--primary").text)
    urls.append(item.find("div", class_="s-item__info clearfix").a.get("href"))

solds = []
newlist = []
newlist2 = []
for url in urls:
    ind_source = requests.get(url).text
    ind_soup = BeautifulSoup(ind_source, "lxml")
    try:
        sold = ind_soup.find("span", class_="qtyTxt vi-bboxrev-dsplblk vi-qty-fixAlignment feedbackON").text.strip()
        #spaces in the class are reduced to one space
        solds.append(sold)
        print(sold)
    except:
        solds.append("error")
        print("error")
for sold in solds:
    newlist.append(sold.split(" sold")[0])
for new in newlist:
    splitted = new.split('\n')[-1]
    removedcomma = splitted.replace(",", "")
    newlist2.append(removedcomma)
for (i,new2) in enumerate(newlist2):
    try:
        if int(new2) <=40000:
            pass
    except:
        newlist2[i] = "0"

FinalArray = []
for name, price, sold in zip(names, prices, newlist2):
    FinalArray.append({"Name of Product": name, "Price": price, "Items sold": sold})
df = pd.DataFrame(FinalArray)
df.to_csv("newbalance.csv")