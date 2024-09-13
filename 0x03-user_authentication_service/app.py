#!/usr/bin/env python3
"""
Flask APP
"""

from flask import Flask, jsonify, request
from auth import Auth
from db import DB


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def start() -> str:
    """
    single GET route ("/") and use flask.jsonify
    to return a JSON payload of the form:
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """
    single POST route ("/users") and use flask.jsonify
    to return a JSON payload of the form:
    """
    
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}, 400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
