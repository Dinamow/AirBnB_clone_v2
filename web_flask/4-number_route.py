#!/usr/bin/python3
"""this is the flask number"""
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
    """home c function"""
    text = text.replace("_", " ")
    return f"C {text}"


@AirBnB.route("/python", strict_slashes=False)
@AirBnB.route("/python/<text>", strict_slashes=False)
def pythonpage(text="is cool"):
    """home python function"""
    text = text.replace("_", " ")
    return f"Python {text}"


@AirBnB.route("/number/<int:n>", strict_slashes=False)
def numperpage(n):
    """home number function"""
    return f"{n} is a number"


if __name__ == "__main__":
    AirBnB.run(host="0.0.0.0", port=5000)
