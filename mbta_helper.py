# Your API KEYS (you need to use your own keys - very long random characters)
import json
import urllib.request
from config import MAPQUEST_API_KEY, MBTA_API_KEY
from pprint import pprint

# , MBTA_API_KEY


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# imports


# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data

### Test Code ###

# url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
# json_object = get_json(url)
# print(json_object['results'][0]['locations'][0]['latLng'])


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """

    # url = f'http://www.mapquestapi.com/geocoding/v1/address?{key1}&{key2}'
    place_name = str(place_name)  # just in case
    construct_url = place_name.replace(" ", "%20")
    # construct_url = clean_input(place_name)

    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={construct_url}'

    lat_long = get_json(url)
    lat_long_dict = lat_long['results'][0]['locations'][0]['latLng']

    return lat_long_dict.get('lat', 0), lat_long_dict.get('lng', 0)

### Test code ###

# lat_long_object = get_lat_long('60 Devonshire St Boston MA')
# print(type(lat_long_object))


# lat_value = str(get_lat_long('60 Devonshire St Boston MA')[0])
# long_value = str(get_lat_long('60 Devonshire St Boston MA')[1])

# print(lat_value, long_value)

# new_url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={lat_value}&filter%5Blongitude%5D={long_value}"
# new_json = get_json(new_url)
# print(new_json)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    lat_value = str(latitude)
    long_value = str(longitude)
    # return lat_value, long_value

    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={lat_value}&filter%5Blongitude%5D={long_value}"

    nearest_station = get_json(url)
    access = nearest_station['data'][0]
    access_name = access["attributes"]['name']
    access_wheelchair = access['attributes']['wheelchair_boarding']

    if access_wheelchair == 2:
        access_wheelchair = 'This station is not accessible to individuals on wheelchairs'
    elif access_wheelchair == 1:
        access_wheelchair = 'This station is accessible to individuals on wheelchairs'
    else:
        access_wheelchair = 'There is no conclusive information regarding whether or not this station is accessible to individuals on wheelchairs'

    return access_name, access_wheelchair


### Test Code ###

# print(get_nearest_station(lat_value, long_value))
# print(type(get_nearest_station(lat_value, long_value)))


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    get_lat_long(place_name)
    lat_value = str(get_lat_long(place_name)[0])
    long_value = str(get_lat_long(place_name)[1])

    final_values = get_nearest_station(lat_value, long_value)

    return final_values

# print(find_stop_near('60 Devonshire St Boston MA'))

def main():
    """
    You can test all the functions here
    """
    # place_name = input(
    #     "Please enter your input just with whitespace and without ','\nWhere are you right now? ")
    user_input = '60 Devonshire St Boston MA'
    # lat_long = get_lat_long(user_input)
    # pprint(lat_long)


    # latitude_value = str(get_lat_long(user_input)[0])
    # longitude_value = str(get_lat_long(user_input)[1])


    # print(latitude_value)
    # print(longitude_value)
    # print(get_nearest_station(latitude_value, longitude_value))
    print(find_stop_near(user_input))


if __name__ == '__main__':
    main()
