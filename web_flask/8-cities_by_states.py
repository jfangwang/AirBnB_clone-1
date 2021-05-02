#!/usr/bin/python3
"""Starts Flaks part 2"""
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    """hello even or odd number"""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
