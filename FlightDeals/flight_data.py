class FlightData:
    def __init__(self, data):
        flight_data = data
        self.out_data = []
        for data_object in flight_data:
            flight_deal = {
                "price": data_object[0]["price"]["total"],
                "details": []
            }
            for itinerary in data_object[0]["itineraries"]:
                flight = []
                for segment in itinerary["segments"]:
                    departure = {
                        "departure": {
                            "airport": segment["departure"]["iataCode"],
                            "time": segment["departure"]["at"]
                        }
                    }
                    arrival = {
                        "arrival": {
                            "airport": segment["arrival"]["iataCode"],
                            "time": segment["arrival"]["at"]
                        }
                    }
                    flight.append(departure)
                    flight.append(arrival)
                flight_deal["details"].append(flight)
            self.out_data.append(flight_deal)
