#!/usr/bin/python3
#this is flask script
from flask import Flask

AirBnB = Flask(__name__)

@AirBnB.route("/", strict_slashes=False)
def homepage():
    return "Hello HBNB!"

if __name__ == "__main__":
    AirBnB.run(host="0.0.0.0" ,port=5000)
