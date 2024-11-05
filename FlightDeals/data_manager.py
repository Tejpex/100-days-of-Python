import os
import requests
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("SHEETY_URL")


class DataManager:
    def __init__(self):
        response = requests.get(URL)
        self.data = response.json()["prices"]
        self.cities = [destination["city"] for destination in self.data]

    def add_city_codes(self, codes):
        for i in range(len(codes)):
            params = {
                "price": {
                    "city": self.data[i]["city"],
                    "iataCode": codes[i],
                    "lowestPrice": self.data[i]["lowestPrice"]
                }
            }
            response = requests.put(f"{URL}/{i+2}", json=params)
            print(response.text)
