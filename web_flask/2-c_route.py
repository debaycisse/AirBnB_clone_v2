#!/usr/bin/python3
"""This module houses the definition of a
flask application with 3 routes"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """handles and processes a query to a route /"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """handles and processes a query to a route /hbnb"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """handles and processes a query to a route /c/<text>"""
    return "C {}".format(text.replace('_', ' '))


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000)
