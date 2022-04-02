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


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """

    # url = f'http://www.mapquestapi.com/geocoding/v1/address?{key1}&{key2}'
    construct_url = place_name.replace(" ", "%20")
    # construct_url = clean_input(place_name)

    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={construct_url}'

    lat_long = get_json(url)
    # return lat_long

    return lat_long['results'][0]['locations'][0]['latLng']


def clean_input(place_name):

    pass


def get_lat(lat_long):
    lat = lat_long.get("lat")
    return lat


def get_long(lat_long):
    long = lat_long.get("lng")
    return long


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

    url = f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={lat_value}&filter%5Blongitude%5D={long_value}"
    # url = f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D=42.358191&filter%5Blongitude%5D=-71.057294"
    # url = f'https://api-v3.mbta.com/stops?{MBTA_API_KEY}filter%5Blatitude%5D={lat_value}&filter%5Blongitude%5D={long_value}'
    # return url 
    nearest_station = get_json(url)
    access = nearest_station['data'][0]
    access_name = access["attributes"]['name']
    access_wheelchair = access['attributes']['wheelchair_boarding']

    return access_name, access_wheelchair


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    user_input = place_name 
    lat_long = get_lat_long(user_input)
    latitude_value = get_lat(lat_long)
    longitude_value = get_long(lat_long)
    nearest_station = get_nearest_station(latitude_value, longitude_value)

    return nearest_station


def main():
    """
    You can test all the functions here
    """
    # place_name = input(
    #     "Please enter your input just with whitespace and without ','\nWhere are you right now? ")
    # user_input = '60 Devonshire St Boston MA'
    user_input = '99 Myrtle St Boston MA 02114'
    # print(clean_input(place_name))
    # lat_long = get_lat_long(user_input)
    # pprint(lat_long)
    # latitude_value = get_lat(lat_long)
    # longitude_value = get_long(lat_long)
    # print(latitude_value)
    # print(longitude_value)
    # print(get_nearest_station(latitude_value, longitude_value))
    near_stop = find_stop_near(user_input)
    print(f'Nearest Station: {near_stop[0]}. \nWheelchair Accessibility: {near_stop[1]}')



if __name__ == '__main__':
    main()
