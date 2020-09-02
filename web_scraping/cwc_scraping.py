from bs4 import BeautifulSoup
import requests

source = requests.get("http://www.cwchu.cuhk.edu.hk/en-gb/prospective-students/why-cw-chu-college").text
soup = BeautifulSoup(source, "lxml")

row = soup.find_all("tr")

print(row)