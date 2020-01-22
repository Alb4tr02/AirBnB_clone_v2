#!/usr/bin/python3

""" script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ resturn string content """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ resturn string content """
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def hello_c(text):
    """ resturn string content """
    m = text.replace("_", " ")
    return 'C %s' % m

if __name__ == '__main__':
    app.run()
