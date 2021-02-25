"""
Module managing the GoogleMaps API requests
"""
import requests
import os
from random import choice
from boto.s3.connection import S3Connection
from answers.const_answers import ERRORS

class GoogleMapsApi():
    """
    Class made to manage the requests to the API and return them.
    Methods:
    * get_lat_lng(address):
        This method returns takes the searched address and returns
        either the latitude and longitude of the desired location
        or an error message if it fails.
        * Arguments:
            - address : corresponds to the parsed address the user
            has entered.
    * get_request_address(address):
        This method returns the address of the desired location in
        the form of a dictionary. If it fails, it returns a
        warning message.
        * Arguments:
            - address : corresponds to the parsed address the user
            has entered.
    """
    def __init__(self):
        pass
    
    def get_lat_lng(self, address):
        """
        This method returns takes the searched address and returns
        either the latitude and longitude of the desired location
        or an error message if it fails.
        * Arguments:
            - address : corresponds to the parsed address the user
            has entered.
        * Return:
            - result : contains a dictionary from a json request
            containing the latitude (lat) and the longitude (lng)
            of the location.
        """
        api_key = S3Connection(os.environ.get["API"])
        url = f"""
        https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}
        """
        for i in range(999999999):
            print(api_key)
        request = requests.get(url)
        jsonrequest =  request.json()
        try:
            result = jsonrequest["results"][0]["geometry"]["location"]
            return result
        except IndexError:
            return choice(ERRORS)
    
    def get_request_address(self, address):
        """
        This method returns the address of the desired location in
        the form of a dictionary. If it fails, it returns a
        warning message.
        * Arguments:
            - address : corresponds to the parsed address the user
            has entered.
        * Return:
            - street_number : street number from the desired address
            extracted from the request (json)
            - street_name : street name from the desired address
            extracted from the request (json)
            - city : city name from the desired address
            extracted from the request (json)
        """
        url = f"""
        https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=AIzaSyDPJtzrcOw2vT2zAVpENBzC7s4CkunsTfc
        """
        request = requests.get(url)
        jsonrequest =  request.json()
        try:
            street_number = jsonrequest["results"][0]["address_components"][0]["long_name"]
            street_name = jsonrequest["results"][0]["address_components"][1]["long_name"]
            city = jsonrequest["results"][0]["address_components"][2]["long_name"]
        except IndexError:
            street_number = None
            street_name = None
            city = None
            return {
            "street_number" : "Aucune ",
            "street_name" : "adresse ",
            "city" : "trouvée. (si t'as recherché une ville ou un pays, c'est normal!)"
        }

        return {
            "street_number" : street_number,
            "street_name" : street_name,
            "city" : city
        }
    
    def get_api_key(self):
        api_key = S3Connection(os.environ.get["API"])
        return api_key