import requests
from flight_data import FlightData
import os

tequila_endpoint = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_KEY")

tequila_header = {
    "apikey": TEQUILA_API_KEY,
}

class FlightSearch:
    def get_dest_code(self, city):
        tequila_parameters = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=f"{tequila_endpoint}/locations/query", params=tequila_parameters, headers=tequila_header)
        tequila_data = response.json()["locations"]
        code = tequila_data[0]["code"]
        return code

    def check_for_flights(self, from_city_code, to_city_code, from_time, to_time):
        check_flight_parameters = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=f"{tequila_endpoint}/v2/search", params= check_flight_parameters, headers=tequila_header)

        try:
            data = response.json()["data"][0]
        except IndexError:
            check_flight_parameters["max_stopovers"] = 1
            response = requests.get(url=f"{tequila_endpoint}/v2/search", params=check_flight_parameters,
                                    headers=tequila_header)
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights to {to_city_code}.")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    from_city=data["route"][0]["cityFrom"],
                    from_airport=data["route"][0]["flyFrom"],
                    to_city=data["route"][0]["cityTo"],
                    to_airport=data["route"][0]["flyTo"],
                    from_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    in_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.to_city}: ${flight_data.price}")
                return flight_data

        else:
            flight_data = FlightData(
                price = data["price"],
                from_city = data["route"][0]["cityFrom"],
                from_airport = data["route"][0]["flyFrom"],
                to_city = data["route"][0]["cityTo"],
                to_airport = data["route"][0]["flyTo"],
                from_date = data["route"][0]["local_departure"].split("T")[0],
                return_date = data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.to_city}: ${flight_data.price}")
            return flight_data
