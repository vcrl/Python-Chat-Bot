"""
Python file used to test the methods from the class
GoogleMapsApi using pytest.
"""

from .googlemaps import GoogleMapsApi
import urllib.request

api = GoogleMapsApi()

def test_get_lat_lng(monkeypatch):
    """
    Test function to test the method "get_lat_lng"
    """
    assert api.get_lat_lng("paris")["lat"] == 48.856614
    assert api.get_lat_lng("paris")["lng"] == 2.3522219
    assert api.get_lat_lng("lille")["lat"] == 50.62925
    assert api.get_lat_lng("lille")["lng"] == 3.057256
    assert api.get_lat_lng("mont+saint+michel")["lat"] == 48.636063
    assert api.get_lat_lng("mont+saint+michel")["lng"] == -1.511457

    result = {
        "lat" : 48.636063,
        "lng" : -1.511457,
    }

    def mockreturn():
        return result
    monkeypatch.setattr("apis.googlemaps.GoogleMapsApi.get_lat_lng", result)
    assert api.get_lat_lng == result

def test_get_request_address(monkeypatch):
    """
    Test function to test the method "get_request_address"
    """
    assert api.get_request_address("mont+saint+michel") == {'city': 'Normandy', 'street_name': 'Manche', 'street_number': 'Mont Saint-Michel'}
    assert api.get_request_address("monoprix+fontainebleau") == {'city': 'Fontainebleau', 'street_name': 'Rue du Château', 'street_number': '23'}
    assert api.get_request_address("notre+dame+paris") == {'city': 'Paris', 'street_name': 'Parvis Notre Dame - Place Jean-Paul II', 'street_number': '6'}

    result = {
        "city" : "Normandy",
        "street_name" : "Manche",
        "street_number" : "Mont Saint-Michel"
    }

    def mockreturn():
        return result
    monkeypatch.setattr("apis.googlemaps.GoogleMapsApi.get_request_address", result)
    assert api.get_request_address == result