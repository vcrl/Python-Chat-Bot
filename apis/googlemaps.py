import googlemaps

class GoogleMapsApi():
    def __init__(self):
        self.gmaps = googlemaps.Client(key='AIzaSyDPJtzrcOw2vT2zAVpENBzC7s4CkunsTfc')
    
    def get_api_request(self, request):
        return self.gmaps.geocode(request)

    def get_maps_url(self, params):
        if params:
            return f"https://www.google.com/maps/search/?api=1&query={params}"
