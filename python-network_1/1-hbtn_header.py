#!/usr/bin/python3
"""
This module contains a script that accepts a URL as a command-line argument,
sends an HTTP request to it, and retrieves the 'X-Request-Id' header value.
"""
import sys
import urllib.request


def get_header_value():
    """
    Sends a request to the provided URL and extracts the specific header
    value 'X-Request-Id' using the dictionary get method.
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        # Utilizing .get() as required by project specifications
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_header_value()
