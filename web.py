from flask import Flask, render_template, request, jsonify
import googlemaps
import json
from wordparser.parser import Parser
from apis.googlemaps import GoogleMapsApi
from apis.wikipedia import Wikipedia

app = Flask(__name__)
word_parser = Parser()
google_api = GoogleMapsApi()
wiki_api = Wikipedia()

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/getuserdata', methods=['POST'])
def getUserData():
    data = request.form['userinput']
    parsed_data = word_parser.parse_input(data)
    tostring_data = ""
    for word in parsed_data:
        tostring_data += f"+{word}"
    lat = google_api.get_api_request(tostring_data)["lat"]
    lng = google_api.get_api_request(tostring_data)["lng"]
    wiki_info = wiki_api.get_api_request(lat, lng, tostring_data)
    wiki_answer = wiki_api.return_place_info(wiki_info)
    return jsonify({
                    'answer':f"Voici un fact : </br><b>{wiki_info}</b></br><justify>{wiki_answer}.</justify>",
                    'lat':lat,
                    'lng':lng
                    })