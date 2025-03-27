import requests
import yaml
import json

# Open the config.yml file and load its contents into the 'config' variable
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

API_KEY = config["apiKey"]
ORG_ID = config["organisationId"]

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

URL = f"https://api.meraki.com/api/v1/organizations/{ORG_ID}/devices?productTypes[]=wireless"

PAYLOAD = None

response = requests.request('GET', URL, headers= HEADERS, data = PAYLOAD)

ap_list = response.json()

for ap in ap_list:
    serial = ap["serial"]
    URL = f"https://api.meraki.com/api/v1/devices/{serial}/reboot"
    response = requests.request('POST', URL, headers= HEADERS, data = PAYLOAD)
    print("AP",serial,"reboot status",response.status_code)