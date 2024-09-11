# import requests

# API_ID = "51aa65a8"
# API_KEY = "b834c4d14e4e3ef440ac2ff6c8871e25"

# API_ENDPOINT = "https://trackapi.nutritionix.com" + "/v2/natural/exercise"

# API_HEADER = {
#     "x-app-id": API_ID,
#     "x-app-key": API_KEY
# }

# API_PARAMETERS = {
#     "query": "walkinng",
#     "gender": "male",
#     "weight_kg": 48,
#     "height_cm": 150,
#     "age": 17    
# }

# response = requests.post(url=API_ENDPOINT, json=API_PARAMETERS, headers=API_HEADER)

# print(response.json())

import requests
from datetime import datetime

APP_ID = "51aa65a8"
API_KEY = "b834c4d14e4e3ef440ac2ff6c8871e25"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_SHEETY_ENDPOINT = "https://api.sheety.co/eda9d35228932e873949c3b8929eb2d5/myWorkouts/workouts"

headers = {
"x-app-id": APP_ID,
"x-app-key": API_KEY
}
GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 173
AGE = 19

sentence = input("Tell me which exercise you did? ")
parameters = {
"query": sentence,
"gender": GENDER,
"weight_kg": WEIGHT_KG,
"height_cm": HEIGHT_CM,
"age": AGE
}

response = requests.post(url=API_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

todayDate = datetime.now().strftime("%d/%m/%Y")
nowTime = datetime.now().strftime("%X")

for excercise in result["exercises"]:
    sheetsInputs = {
        "workout": {
            "date": todayDate,
            "time": nowTime,
            "exercise": excercise["name"].title(),
            "duration": excercise["duration_min"],
            "calories": excercise["nf_calories"]
        }
    }

    sheetsResponse = requests.post(url=API_SHEETY_ENDPOINT, json=sheetsInputs)

    print(sheetsResponse.text)