import os
import requests
import smtplib
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

my_email = os.getenv("MY_EMAIL")
my_email_password = os.getenv("SMTP_PASSWORD")
smtp_address = os.getenv("SMTP_ADDRESS")


class NotificationManager:
    def __init__(self, flight_data):
        data = flight_data
        self.messages = []
        for flight in data:
            flight_start = flight["details"][0][0]["departure"]
            start_date = flight_start["time"].split("T")[0]
            flight_end = flight["details"][1][0]["departure"]
            end_date = flight_end["time"].split("T")[0]
            self.messages.append(f"Subject: Low price alert! \n\n Only {flight["price"]} EURO to fly from "
                                 f"{flight_start["airport"]} to {flight_end["airport"]}, "
                                 f"on {start_date} until {end_date}.")
        print(self.messages)

    def send_sms_message(self):
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

    def send_emails(self, email_list):
        for email in email_list:
            for message in self.messages:
                with smtplib.SMTP(smtp_address, port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=my_email_password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=email,
                                        msg=message
                                        )
