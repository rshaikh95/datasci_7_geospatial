import requests 
import urllib.parse
import json
import pandas as pd

data = pd.read_csv (r'/home/rahil_shaikh/datasci_7_geospatial/assignment7_slim_hospital_addresses.csv')   

list_of_address = [data

]

google_response = []

for address in list_of_address: 
    api_key = 'AIzaSyB0K9kFuiTKI6ZzM2qADE8TaQHmOkGRC9s'

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    print(f'....finished with {address}')


df1 = pd.DataFrame(google_response)
df1
##### reverse code 

reverse_geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
latitude = '38.897676'
longitude = '-77.036530'
step1 = reverse_geocode_url + latitude + ',' + longitude + '&key=' + api_key

###### function

def geocode(address_here): 

    api_key = 'AIzaSyB0K9kFuiTKI6ZzM2qADE8TaQHmOkGRC9s'

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address_here
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address_here, 'lat': lat_response, 'lon': lng_response}

    return final 


geocode('5 bleecker st ny ny')

