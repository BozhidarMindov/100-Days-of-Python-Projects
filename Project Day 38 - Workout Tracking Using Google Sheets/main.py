import requests
from datetime import datetime
import os

#---------------------------------Nutritionix API--------------------------------------
APP_ID = os.environ.get("NUTRITION_APP_ID")
API_KEY = os.environ.get("NUTRITION_API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": "70",
    "height_cm": "175",
    "age": "20"
}

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(api_endpoint, json=parameters, headers=headers)
output = response.json()
print(output)

#----------------------------------Sheety API----------------------------------------
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("TOKEN_SHEETY")

today = datetime.now().strftime("%d/%m/%Y")
curr_time = datetime.now().strftime("%X")

for exercise in output["exercises"]:
    sheets_input = {
        "workout": {
            "date": today,
            "time": curr_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    sheet_response = requests.post(sheety_endpoint, json= sheets_input,headers=sheety_headers)
    print(sheet_response.text)
