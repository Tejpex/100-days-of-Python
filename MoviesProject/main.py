import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
movies = soup.select(selector=".gallery h3")
list_of_titles = [movie.getText().replace("â\x80\x93", "-") for movie in movies]
list_of_titles.reverse()

with open("movies.txt", mode="w") as movie_list:
    movie_list.write("\n".join(list_of_titles))
