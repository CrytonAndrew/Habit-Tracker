import requests
from decouple import config
from datetime import datetime

USERNAME = "cryton"
TOKEN = config("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"}

# create_user_response = requests.post(pixela_endpoint, json=user_params)
# print(create_user_response.text)

GRAPH_ID = "graph1"
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}
graph_headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_endpoint, headers=graph_headers, json=graph_params)
# print(graph_response.text)

# get_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_NAME}"
# get_graph_response = requests.get(url=get_graph_endpoint)

post_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many commits did you make today >")
}


post_response = requests.post(url=post_graph_endpoint, json=post_params, headers=graph_headers)
print(post_response.text)

# Update a piece of state for a certain day

# update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20210102"
# update_params = {
#     "quantity": "3"
# }
# update_response = requests.put(url=update_endpoint, json=update_params, headers=graph_headers)
# print(update_response.text)

