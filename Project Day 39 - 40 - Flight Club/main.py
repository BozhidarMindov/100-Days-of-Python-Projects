#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for i in sheet_data:
        i["iataCode"] = flight_search.get_dest_code(i["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_dest_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(2 * 30))

for country in sheet_data:
    flight = flight_search.check_for_flights("SOF", country["iataCode"], from_time=tomorrow, to_time=six_month_from_now)
    if flight is not None and flight.price < country["lowestPrice"]:
        users = data_manager.get_customer_info()
        emails = [name["email"] for name in users]
        names = [name["firstName"] for name in users]

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.from_airport}.{flight.to_airport}.{flight.from_date}*{flight.to_airport}.{flight.from_airport}.{flight.return_date}"

        if flight.stop_overs > 0:
            f"\n\nFlight has {flight.stop_overs}, via {flight.in_city}."
            notification_manager.send_notification(emails = emails,
                msg=f"Subject: Low Flight Price Alert\n\nOnly ${flight.price} to fly from {flight.from_city}{flight.from_airport} to {flight.to_city}{flight.to_airport}\nDate is from {flight.from_date} to {flight.return_date}\nFlight has {flight.stop_overs} stopovers, via {flight.in_city}.\n{link}")
        else:
            notification_manager.send_notification(emails=emails, msg = f"Subject: Low Flight Price Alert\n\nOnly ${flight.price} to fly from {flight.from_city}{flight.from_airport} to {flight.to_city}{flight.to_airport}\nDate is from {flight.from_date} to {flight.return_date}\n{link}")
