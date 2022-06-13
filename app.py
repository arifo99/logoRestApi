import flask
import json
from flask import request
from bingScraper import BingScraper

app = flask.Flask(__name__)
searchEngine = BingScraper()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello!</h1>"

@app.route('/get_logo', methods=['GET'])
def getPosts():
    company = request.args.get('company')

    return json.dumps(searchEngine.getLogoLink(company))

if __name__ == "__main__":
    app.run()
