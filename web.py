from flask import Flask, render_template, request, jsonify
import json
from wordparser.parser import Parser

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/getuserdata', methods=['POST'])
def getUserData():
    data = request.form['userinput']
    #parser = Parser()
    #print(parser.parse_input(data))
    return json.dumps({'status':'OK', 'input':data})