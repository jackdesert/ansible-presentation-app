from flask import Flask
from flask import make_response
from flask import render_template
import requests
import pdb

app = Flask(__name__)

def ip_address():
    try:
        address = requests.get('https://ipecho.net/plain', timeout=2).text
    except:
        # TODO only rescue from specific exceptions
        address = 'unknown'
    return address



@app.route("/")
def hello():
    response = make_response(render_template('index.jj2', ip_address=ip_address()))
    return response

if __name__ == "__main__":
    app.run()
