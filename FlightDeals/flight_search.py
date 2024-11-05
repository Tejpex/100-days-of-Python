import os
import requests
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AMADEUS_API_KEY")
API_SECRET = os.getenv("AMADEUS_API_SECRET")
BASE_URL = os.getenv("AMADEUS_BASE_URL")

AIRPORT_FROM = "CPH"
NUMBER_ADULTS = 1

tomorrow = date.today() + timedelta(days=1)
aWeekFromTomorrow = date.today() + timedelta(days=8)


class FlightSearch:
    def __init__(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }

        response = requests.post(f"{BASE_URL}/v1/security/oauth2/token", data=params, headers=headers)
        self.flight_token = response.json()["access_token"]

    def find_flight_deals(self, data):
        flight_deals = []
        deals_header = {
            "Authorization": f"Bearer {self.flight_token}"
        }
        for destination in data:
            deals_params = {
                "originLocationCode": AIRPORT_FROM,
                "destinationLocationCode": destination["iataCode"],
                "departureDate": str(tomorrow),
                "returnDate": str(aWeekFromTomorrow),
                "adults": NUMBER_ADULTS,
                "currencyCode": "EUR",
                "maxPrice": destination["lowestPrice"],
                "max": 1
            }
            deals_response = requests.get(f"{BASE_URL}/v2/shopping/flight-offers",
                                          params=deals_params, headers=deals_header)
            deal = deals_response.json()
            if "data" in deal and len(deal["data"]) > 0:
                flight_deals.append(deal["data"])

        return flight_deals

    def find_city_codes(self, cities):
        codes = []
        city_header = {
            "Authorization": f"Bearer {self.flight_token}"
        }
        for city in cities:
            city_params = {
                "keyword": city
            }
            response = requests.get(f"{BASE_URL}/v1/reference-data/locations/cities",
                                    params=city_params, headers=city_header)
            codes.append(response.json()["data"][0]["iataCode"])

        return codes
