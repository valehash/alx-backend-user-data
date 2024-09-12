#!/usr/bin/env python3
"""
Flask APP
"""

from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/", methods=["GET"], strict_slashes=False)
def start() -> str:
    """
     single GET route ("/") and use flask.jsonify 
     to return a JSON payload of the form:
    """
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
