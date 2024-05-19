#!/usr/bin/python3
"""This modules houses a definition of a flask
application, along with 7 routes that it handles"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """processes and handles a query to route '/'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """processes and handles a query to route '/hbnb'"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """handles and processes a query to route '/c/<text>'
    where is a parameter to this function"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """handles and processes both query to route /python
    (with its default parameter) and /python/<text>"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number_n(n):
    """handles and processes a query to route '/number/<n>', which
    only processes a query or request when the passed parameter
    is a type of integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template_n(n):
    """handles and processes a query to route '/number_template/<int:n>'.
    It renders or displays the contents of a specified HTML file,
    stored in templates folder"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even_n(n):
    """handles and processes a query to '/number_odd_or_even/<int:n>' by
    rendering contents of a specified HTML file, stored in
    templates folder"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
