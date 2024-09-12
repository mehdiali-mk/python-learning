import requests
from bs4 import BeautifulSoup

userChoiceDate = input("On which date you want to travel?\nEnter the date in YYYY-MM-DD Format = ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{userChoiceDate}/")

websiteCode = response.text
soup = BeautifulSoup(websiteCode, "html.parser")

rawNamesOfSongs = soup.findAll(name="h3")

for name in rawNamesOfSongs:
    print(name)

# songsNameList = [str(name.getText()) for name in rawNamesOfSongs]
# print(songsNameList)