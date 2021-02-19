import requests
from random import choice

class Wikipedia():
    def __init__(self):
        pass
    
    def get_api_request(self, lat, lng, user_search):
        url = "https://fr.wikipedia.org/w/api.php"
        params = {"action": "query", "list": "geosearch", "gsradius": "10000",
                    "gscoord": f"{lat}|{lng}", "format": "json"}
        request = requests.get(url, params=params).json()
        tosearch = request["query"]["geosearch"]

        for place in tosearch:
            if place["title"] != user_search:
                tosearch = place
        if tosearch:
            title = tosearch["title"]
            return title
        return "Error"

    def return_place_info(self, title):
        url = f"https://fr.wikipedia.org/api/rest_v1/page/summary/{title}"
        request = requests.get(url).json()
        place_info = request["extract"]
        link = request["content_urls"]["desktop"]["page"]
        bot_answer = place_info + "</br>" + f"<a href='{link}'>{link}</a>"
        return bot_answer