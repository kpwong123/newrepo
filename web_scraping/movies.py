from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://www.rottentomatoes.com/top/").text
soup = BeautifulSoup(source, "lxml")


movie_list = soup.find_all("table", class_="movie_list")[2]

movies = movie_list.find_all("tr")


movie_score = []
movie_title = []
movie_url = []
for movie in movies:
    score = movie.find("span", class_="tMeterScore").text
    title = movie.find("a").text
    url = movie.a.get("href")
    movie_score.append(score)
    movie_title.append(title)
    movie_url.append(url)

movie_concensus = []
movie_director = []
movie_release_date = []
for real in movie_url:
    page_source = requests.get("https://www.rottentomatoes.com" + real).text
    page_soup = BeautifulSoup(page_source, "lxml")
    concensus = page_soup.find("p", class_="mop-ratings-wrap__text mop-ratings-wrap__text--concensus").text
    director = page_soup.find("ul", class_="content-meta info").find_all("li")[2].a.text
    release_date = page_soup.find("ul", class_="content-meta info").find_all("li")[4].time.text
    stripped = release_date.replace("\n", "").strip()
    movie_concensus.append(concensus)
    movie_release_date.append(stripped)
    movie_director.append(director)

final_array = []
for title, score, concensus, director, date in zip(movie_title, movie_score, movie_concensus, movie_director, movie_release_date):
    final_array.append({"Title": title, "Score": score, "Concensus of Reviewers": concensus, "Director": director, "Release Date": date})

df = pd.DataFrame(final_array)

df.to_csv("movie_review.csv")
    

# print(real_url)

# print(movie_score, movie_title, movie_url)
