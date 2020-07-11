from flask import Flask
from flask import request
from flask import jsonify

from lib.parser import Parser

app = Flask(__name__)

@app.route('/')
def hello_world():
    text = request.args.get('text')
    parser = Parser()
    result = parser.parse(text)

    return jsonify(result)