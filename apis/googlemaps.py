import googlemaps
import requests

class GoogleMapsApi():
    def __init__(self):
        pass
    
    def get_api_request(self, address):
        url = f"""
        https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=AIzaSyDPJtzrcOw2vT2zAVpENBzC7s4CkunsTfc
        """
        request = requests.get(url)
        jsonrequest =  request.json()
        result = jsonrequest["results"][0]["geometry"]["location"]
        return result

