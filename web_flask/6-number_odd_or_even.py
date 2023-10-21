#!/usr/bin/python3
"""this is the flask odd or even"""
from flask import Flask, render_template


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


@AirBnB.route("/number_template/<int:n>", strict_slashes=False)
def NumperHtmlpage(n):
    """home number html function"""
    return render_template('5-number.html', number=n)


@AirBnB.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def OddOrEvenHtmlpage(n):
    """home number odd or even html function"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    AirBnB.run(host="0.0.0.0", port=5000)
