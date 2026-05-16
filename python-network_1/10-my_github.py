#!/usr/bin/python3
"""
This module contains a script that uses the GitHub API to display a user's ID.
It utilizes Basic Authentication with a personal access token.
"""
import sys
import requests


def display_github_id():
    """
    Authenticates with the GitHub API using credentials from command line
    arguments and prints the account's numeric ID if successful.
    """
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    # Using HTTP Basic Authentication tuple with requests
    response = requests.get(url, auth=(username, token))

    try:
        json_data = response.json()
        # Using dictionary .get() method to access keys safely
        print(json_data.get("id"))
    except ValueError:
        print("None")


if __name__ == "__main__":
    display_github_id():
