#!/usr/bin/python3
"""this is the flask c"""
from flask import Flask


AirBnB = Flask(__name__)


@AirBnB.route("/", strict_slashes=False)
def homepage():
    """home function"""
    return "Hello HBNB!"


@AirBnB.route("/hbnb", strict_slashes=False)
def HBNBpage():
    """HBNH function"""
    return "HBNB"


@AirBnB.route("/c/<text>", strict_slashes=False)
def Cpage(text):
    """c function"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    AirBnB.run(host="0.0.0.0", port=5000)
