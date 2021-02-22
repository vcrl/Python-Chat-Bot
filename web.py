"""
Core of the application : it manages the deployment of the
application on internet.
"""
from flask import Flask, render_template, request, jsonify
import json
from random import choice
from wordparser.parser import Parser
from apis.googlemaps import GoogleMapsApi
from apis.wikipedia import Wikipedia
from answers.const_answers import ANSWERS, ERRORS

app = Flask(__name__)
word_parser = Parser()
google_api = GoogleMapsApi()
wiki_api = Wikipedia()

@app.route('/', methods = ['GET', 'POST'])
def index():
    """
    Index or main page of the web app.
    Returns the template index.html to
    be displayed.
    """
    return render_template('index.html')

@app.route('/getuserdata', methods=['POST'])
def getUserData():
    """
    This functions manages all the
    functionalities corresponding to
    the user data : its input, the returns,
    and the parsing.
    """
    data = request.form['userinput']
    parsed_data = word_parser.parse_input(data)
    tostring_data = ""
    for word in parsed_data:
        tostring_data += f"+{word}"
    try:
        lat = google_api.get_lat_lng(tostring_data)["lat"]
        lng = google_api.get_lat_lng(tostring_data)["lng"]
        address = google_api.get_request_address(tostring_data)
        wiki_info = wiki_api.get_api_request(lat, lng, tostring_data)
        wiki_answer = wiki_api.return_place_info(wiki_info)
        return jsonify({
                        'answer':f"""{choice(ANSWERS)}
                                    </br>
                                    La/le splendide <b>{wiki_info}</b>
                                    </br></br>
                                    <justify>{wiki_answer}.</justify>
                                    </br></br>
                                    <b>...Oh et voilà l'adresse pour y aller
                                    </br></br>
                                    </b>► <u>{address["street_number"]}, 
                                    {address["street_name"]}, {address["city"]}</u>
                                    </br></br>
                                    """,
                        'lat':lat,
                        'lng':lng
                        })
    except TypeError:
        return jsonify({
                        'answer':f"{choice(ERRORS)}",
                        'lat':None,
                        'lng':None
                        })