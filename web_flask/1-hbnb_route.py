#!/usr/bin/python3
"""This module houses a definition of two flask application's routes"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """This function handles and processes a query to route /"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """This function handles and processes a query to route /hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
