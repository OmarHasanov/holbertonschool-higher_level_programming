#!/usr/bin/python3
"""
This module contains a script that sends a POST request with an email
parameter to a given URL using requests, and prints the response body.
"""
import sys
import requests


def post_email_with_requests():
    """
    Sends an HTTP POST request to the URL from sys.argv[1] containing the
    email parameter from sys.argv[2], and displays the response text.
    """
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":
    post_email_with_requests()
