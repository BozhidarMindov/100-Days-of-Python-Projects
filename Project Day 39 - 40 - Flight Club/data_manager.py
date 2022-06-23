import requests
import os

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
sheety_endpoint_users = os.environ.get("SHEETY_ENDPOINT_USERS")
SHEETY_TOKEN = os.environ.get("TOKEN")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {
        }

    def get_data(self):
        response = requests.get(sheety_endpoint, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_dest_code(self):
        for city in self.destination_data:
            updated_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=updated_data,
                headers=sheety_headers
            )

    def get_customer_info(self):
        get_response = requests.get(
            url=sheety_endpoint_users, headers=sheety_headers
        )
        data = get_response.json()
        self.user_data = data["users"]
        return self.user_data
