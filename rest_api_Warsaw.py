import requests
import json

token = 'twoj ApiKey wygenerowany z serwisu https://api.um.warszawa.pl/#'
url = 'https://api.um.warszawa.pl/api/action/busestrams_get/'
resource_id = 'f2e5503e-927d-4ad3-9500-4ab9e55deb59'

bus_params = {
    'apikey':token,
    'type':1,
    'resource_id': resource_id
    }
tram_params = {
    'apikey':token,
    'type':2,
    'resource_id': resource_id
    }

def data_from_um_Warsaw_api():
    response_from_api = requests.get(url = url, params = bus_params)
    json_data = json.loads(response_from_api.text)
    return json_data