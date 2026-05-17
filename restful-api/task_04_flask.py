#!/usr/bin/python3
"""
A simple Flask-based API that manages user data.
Supports various endpoints for status check, data retrieval,
and adding new users via POST requests.
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# İstifadəçilər yaddaşda lüğət (dictionary) kimi saxlanılır
users = {}


@app.route("/")
def home():
    """Returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns the full object for a given username.
    Returns 404 if user not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Parses JSON data to add a new user.
    Handles invalid JSON, missing username, and duplicates.
    """
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Yeni istifadəçini lüğətə əlavə edirik
    users[username] = data

    response = {
        "message": "User added",
        "user": data
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run()
