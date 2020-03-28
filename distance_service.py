import googlemaps
import pprint
import time
import constants
import re

API_KEY = constants.PLACES_API_KEY

gmaps = googlemaps.Client(key = API_KEY)

places_result = gmaps.places_nearby(location = '-33.826987, 151.087309', radius = 800, open_now = False, keyword = 'Coles')

for place in places_result['results']:
  place_id = place['place_id']

  # need to request geometry because otherwise api sends duplicate results, for an example, when searching around
  # rhodes sent 3 coles results, rhodes/wentworth point and sydney olympic park. wentworth point and 
  # sydney olympic park referred to the same place. 
  fields = ['name', 'adr_address', 'formatted_phone_number', 'geometry']

  place_details = gmaps.place(place_id = place_id, fields = fields)

  # print(place_details)
  
  print("Name: ", place_details['result']['name'])
  print("Phone Number: ", place_details['result']['formatted_phone_number'])

  # this is to get the suburb from the adr_address string
  address_string = place_details['result']['adr_address']
  match = re.search('<span class="locality">(.+?)</span>', address_string)
  if match:
    suburb = match.group(1)

  print("Suburb:", suburb, "\r\n")
