#!/usr/bin/python3
"""this is the flask hello"""
from flask import Flask


AirBnB = Flask(__name__)


@AirBnB.route("/", strict_slashes=False)
def homepage():
    """home page function"""
    return "Hello HBNB!"


@AirBnB.route("/hbnb", strict_slashes=False)
def HBNBpage():
    """home HBNH function"""
    return "HBNB"


@AirBnB.route("/c/<text>", strict_slashes=False)
def Cpage(text):
    """home HBNH function"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    AirBnB.run(host="0.0.0.0", port=5000)
