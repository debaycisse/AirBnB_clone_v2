#!/usr/bin/python3
"""This module houses the definition of a flask
application that handles a / route"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function handles the / route of the application."""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
