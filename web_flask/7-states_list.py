#!/usr/bin/python3
"""Starts Flaks part 2"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """teardown"""
    storage.close()


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


@app.route('/number/<int:n>', strict_slashes=False)
def number_text(n):
    """hello number"""
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """hello template number"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even_or_odd(n):
    """hello even or odd number"""
    return render_template("6-number_odd_or_even.html", n=n)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """hello even or odd number"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
