#!/usr/bin/python3
"""this is the flask hello"""
from flask import Flask


AirBnB = Flask(__name__)
AirBnB.url_map.strict_slashes = False


@AirBnB.route("/")
def homepage():
    """home page function"""
    return "Hello HBNB!"


if __name__ == "__main__":
    AirBnB.run(host="0.0.0.0", port=5000)
