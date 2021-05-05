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


@app.route('/states', strict_slashes=False)
def states_asdf():
    """hello states"""
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """hello number"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_appcontext(exception):
    """teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
