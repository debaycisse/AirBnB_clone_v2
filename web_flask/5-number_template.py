#!/usr/bin/python3
"""This modules houses a definition of a flask
application that contains 6 different routes"""

from flask import Flask
from flask import render_template

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


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """handles and processes a query to route /python/<text>"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number_n(n):
    """handles and processes a query to route /number/<n>"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """handles and processes a query to route /number_template/<n>"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
