#!/usr/bin/python3
"""Starts Flaks part 2"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """hello world"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hello HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """hello text"""
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """hello text"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route('/number/<n>', strict_slashes=False)
def number_text(n):
    """hello number"""
    if n.isdecimal():
        return n + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
