import os
import requests
from sinch import SinchClient
from dotenv import load_dotenv

load_dotenv()

sinch_client = SinchClient(
    key_id=os.getenv("SINCH_KEY_ID"),
    key_secret=os.getenv("SINCH_KEY_SECRET"),
    project_id=os.getenv("SINCH_PROJECT_ID")
)

service_plan_id = os.getenv("SINCH_SERVICE_PLAN_ID")
token = os.getenv("SINCH_BEARER_TOKEN")
from_nr = os.getenv("SINCH_FROM_NUMBER")
to_nr = os.getenv("MY_NUMBER")


class NotificationManager:
    def __init__(self, flight_data):
        data = flight_data
        self.messages = []
        for flight in data:
            flight_start = flight["details"][0][0]["departure"]
            start_date = flight_start["time"].split("T")[0]
            flight_end = flight["details"][1][0]["departure"]
            end_date = flight_end["time"].split("T")[0]
            self.messages.append(f"Low price alert! Only €{flight["price"]} to fly from "
                                 f"{flight_start["airport"]} to {flight_end["airport"]}, "
                                 f"on {start_date} until {end_date}.")
        print(self.messages)

    def send_message(self):
        for message in self.messages:
            region = "eu"
            url = "https://" + region + ".sms.api.sinch.com/xms/v1/" + service_plan_id + "/batches"

            payload = {
                "from": from_nr,
                "to": [
                    to_nr,
                ],
                "body": message,
                "delivery_report": "none",
                "type": "mt_text"
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }

            response = requests.post(url, json=payload, headers=headers)
            data = response.json()
            print(data)
