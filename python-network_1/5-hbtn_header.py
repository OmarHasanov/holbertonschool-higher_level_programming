#!/usr/bin/python3
"""
This module contains a script that takes a URL as a command-line argument,
sends an HTTP request using requests, and displays the X-Request-Id header.
"""
import sys
import requests


def get_header_with_requests():
    """
    Sends a GET request to the URL from sys.argv[1] and prints the value
    of the 'X-Request-Id' header variable using the dict get method.
    """
    url = sys.argv[1]
    response = requests.get(url)

    # Utilizing .get() on headers dictionary as required by project specs
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_header_with_requests()
