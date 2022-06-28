import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

#making an url request
response = requests.get(URL)
ym_web_page = response.text

#scraping the needed data
soup = BeautifulSoup(ym_web_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")

#storing the data in a list
movies_texts = []
for movie in movies:
    movies_texts.append(movies.getText())

#reversing the list
movies_texts.reverse()

#writing the list to a text file
with open("movies.txt", "w", encoding="utf-8") as file:
    file.write("TOP 100 MOVIES TO WATCH\n\n")
    for text in movies_texts:
        file.write(f"{text}\n")

