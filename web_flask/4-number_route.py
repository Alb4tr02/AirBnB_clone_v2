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


@app.route('/python/<string:text>', strict_slashes=False)
def hello_python(text):
    """ resturn string content """
    m = text.replace("_", " ")
    return 'Python %s' % m


@app.route('/python/', strict_slashes=False)
def hello_p():
    """ resturn string content """
    return 'Python is cool'


@app.route('/number/<int:n>', strict_slashes=False)
def hello_n(n):
    """ resturn string content """
    return '%d is a number' % n

if __name__ == '__main__':
    app.run()
