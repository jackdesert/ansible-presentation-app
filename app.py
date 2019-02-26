from flask import Flask
from flask import make_response
from flask import render_template
import redis
import requests
import pdb

app = Flask(__name__)
REDIS = redis.StrictRedis(host='localhost', port=6379, db=0)

def ip_address():
    try:
        address = requests.get('https://ipecho.net/plain', timeout=2).text
    except:
        # TODO only rescue from specific exceptions
        address = 'unknown'
    return address

def count():
    value = REDIS.incr('flask-demo-page-loads')
    return value


@app.route("/")
def hello():
    response = make_response(render_template('index.jj2',
                                             ip_address=ip_address(),
                                             page_loads=count()))
    return response

if __name__ == "__main__":
    app.run()
