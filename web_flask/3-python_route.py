#!/usr/bin/python3
"""This module houses a flask application's
definition and its declared routes"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """handles and processes a query to a route /"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """handles and processes a qeury to route /hbnb"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """handles and processes a query to route /c/<text>"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>')
def python_text(text):
    """handles and processes a query to route /python/<text>"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__mian__':
    app.run(host='0.0.0.0', port=5000)
