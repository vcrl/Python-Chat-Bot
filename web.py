from flask import Flask, render_template, request, jsonify
import googlemaps
import json
from wordparser.parser import Parser
from apis.googlemaps import GoogleMapsApi

app = Flask(__name__)
word_parser = Parser()
google_api = GoogleMapsApi()

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
    google_link = google_api.get_maps_url(tostring_data) # API google link
    return jsonify({'input':f"Voici votre requête. </br><a href={google_link}>Lien</a>"})#json.dumps({'status':'OK', 'input':data}) #jsonify(data)