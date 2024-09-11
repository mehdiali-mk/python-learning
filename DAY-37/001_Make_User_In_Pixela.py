import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "Mehdialipixela@123"
USERNAME = "mehdialimk"

PIXELA_PAREMETERS = {
    "token": "Mehdialipixela@123",
    "username": "mehdialimk",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_PAREMETERS)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

GRAPH_ID_1 = "graph1"

GRAPH_PAREMETERS = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

HEADER = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PAREMETERS, headers=HEADER)



PIXELA_ADD_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID_1}"

today = dt.datetime(year=2024, month=8, day=4)
dateToEnter = today.strftime("%Y%m%d")

PIXELA_ADD_PEREMETERS = {
    "date": dateToEnter,
    "quantity": "20.75",
    # "optionalData": "I have cycled 2 km today!!\nJuhapura to D-MART near the Metro station."
}

# response = requests.post(url=PIXELA_ADD_ENDPOINT, json=PIXELA_ADD_PEREMETERS, headers=HEADER)
# print(response.text)

PIXELA_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID_1}/{dateToEnter}"

PIXELA_UPDATE_PARAMETERS = {
    "quantity": "5",
}

response = requests.put(url=PIXELA_UPDATE_ENDPOINT, json=PIXELA_UPDATE_PARAMETERS, headers=HEADER)
print(f"{response.text}")