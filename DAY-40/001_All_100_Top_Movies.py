import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

websiteCode = response.text

soup = BeautifulSoup(websiteCode, "html.parser")

titleNames = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__BfenH")

titleNamesList = [str(names.getText()) for names in titleNames]
titleNamesList = titleNamesList[::-1]

with open("./DAY-40/moviesList.txt", "w") as file:
    for name in titleNamesList:
        name = name.replace(") ", " - ")
        writeName = name + "\n"
        file.writelines(writeName)

