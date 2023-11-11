import requests 
import urllib.parse
import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API')

df = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK7/assignment7_slim_hospital_addresses.csv")

df['gcd'] = df['ADDRESS'] + ' ' + df['CITY'] + ' ' + df['STATE']

df_s =df.sample(n=100)

google_response = []

for address in df_s['gcd']: 
    
    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + api_key

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lng': lng_response}
    
    google_response.append(final)

    print(f'....finished with {address}')

df_geo = pd.DataFrame(google_response)

df_geo.to_csv('geocoding.csv')

##### reverse code 

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK7/assignment7_slim_hospital_coordinates.csv')

df['gcd'] = df['X'].astype(str) + ',' + df['Y'].astype(str)

df_s = df.sample(100)
    
google_response = []

for coord in df_s['gcd']:
    
    location_raw = coord
    location_clean = urllib.parse.quote(location_raw)

    reverse_geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
    step1 = reverse_geocode_url + location_clean + '&key=' + api_key

    response = requests.get(step1)
    response_dictionary = response.json()

    address = response_dictionary['results'][0]['formatted_address']

    final = {'address': address, 'coordinates': coord}
    google_response.append(final)

    print(f'....finished with {coord}')

df_add = pd.DataFrame(google_response)

df_add.to_csv('reverse_geocoding.csv')