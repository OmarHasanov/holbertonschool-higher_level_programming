#!/usr/bin/python3
"""
This module contains a script that sends an HTTP request to a specific URL
using requests and prints the response body, handling error status codes.
"""
import sys
import requests


def fetch_url_status():
    """
    Fetches the content of a URL from sys.argv[1]. Prints the response body
    if successful, or prints an error code if the status code is >= 400.
    """
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_url_status()
