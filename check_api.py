import urllib.request
import json
from pprint import pprint
from config import MAPQUEST_API_KEY

# MAPQUEST_API_KEY = 'YOUR API KEY'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)
print(response_data['results'][0]['locations'][0]['postalCode'])