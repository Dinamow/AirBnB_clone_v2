#!/usr/bin/python3
"""starts a Flask web application:"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """print a number"""
    data = storage.all(State)
    return render_template('7-states_list.html', data=data)


@app.teardown_appcontext
def cleanDb(error=None):
    """close the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
