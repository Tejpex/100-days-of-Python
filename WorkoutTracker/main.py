import requests
import os
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEET_URL = os.environ.get("SHEET_URL")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")

WEIGHT_KG = 65
HEIGHT_CM = 170
AGE = 30

workout_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
workout_headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

exercise = input("Tell me what you did today: ")

workout_params = {
    "query": exercise,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

workout_response = requests.post(workout_url, json=workout_params, headers=workout_headers)
workout_result = workout_response.json()
exercises = workout_result["exercises"]

today = datetime.now()
formatted_date = today.strftime("%Y-%m-%d")
formatted_time = today.strftime("%H:%M")

for item in exercises:
    sheets_url = SHEET_URL
    sheets_headers = {
        "Authorization": f"Bearer {SHEET_TOKEN}"
    }
    sheets_params = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
        }
    }

    sheets_response = requests.post(sheets_url, json=sheets_params, headers=sheets_headers)
    print(sheets_response.text)
