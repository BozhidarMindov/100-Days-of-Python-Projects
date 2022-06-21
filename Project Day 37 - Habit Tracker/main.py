import requests
from datetime import datetime
import os

USER_NAME = "bmindov17"
TOKEN = os.environ.get("PIXEL_TOKEN")
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"


##Creating an account on Pixela
# user_parameters = {
#     "token": TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

##Creating a graph
# graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
#
# graph_parameters = {
#     "id": GRAPH_ID,
#     "name": "Running graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ichou"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

#adding pixels to the graph
today = datetime.now()

pixel_parameters = {
   "date": today.strftime("%Y%m%d"),
   "quantity": input("How many km did you run today?"),
}

pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

pixel_response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)

#updating an existing pixel(changing its data)
# update_parameters = {
#     "quantity": "6.5"
# }
# update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# update_pixel = requests.put(update_pixel_endpoint, json=update_parameters, headers=headers)

#deleteing a pixel
# delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# delete_pixel = requests.delete(delete_pixel_endpoint, headers=headers)
