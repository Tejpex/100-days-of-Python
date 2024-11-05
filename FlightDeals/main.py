from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

user_data_manager = DataManager()
flight_finder = FlightSearch()

# city_codes = flight_finder.find_city_codes(cities=user_data_manager.cities)
# user_data_manager.add_city_codes(city_codes)

flight_deals = flight_finder.find_flight_deals(data=user_data_manager.data)

flight_data_handler = FlightData(flight_deals)
if len(flight_data_handler.out_data) > 0:
    notification_manager = NotificationManager(flight_data_handler.out_data)
    notification_manager.send_message()
