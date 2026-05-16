#!/usr/bin/python3
"""
This module provides a script that fetches the status of the Holberton
School intranet using the requests package.
"""
import requests


def fetch_status_with_requests():
    """
    Fetches the intranet status page using the requests library and prints
    information about the response body, including its type and content.
    """
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_status_with_requests()
