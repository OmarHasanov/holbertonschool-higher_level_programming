#!/usr/bin/python3
"""
This module contains a script that sends a POST request with a letter search
parameter to a local web server API and parses the returned JSON payload.
"""
import sys
import requests


def search_user_api():
    """
    Sends a letter parameter 'q' from command-line input via POST request.
    Validates if response is formatted correctly as a non-empty JSON object.
    """
    url = "http://0.0.0.0:5000/search_user"

    # Set q="" if no argument is given, otherwise take sys.argv[1]
    if len(sys.argv) > 1:
        q_letter = sys.argv[1]
    else:
        q_letter = ""

    payload = {'q': q_letter}

    try:
        response = requests.post(url, data=payload)
        # Attempt to parse the response as JSON
        json_data = response.json()

        if json_data == {} or not json_data:
            print("No result")
        else:
            # Using dictionary .get() method to access keys safely
            user_id = json_data.get("id")
            user_name = json_data.get("name")
            print("[{}] {}".format(user_id, user_name))

    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user_api()
