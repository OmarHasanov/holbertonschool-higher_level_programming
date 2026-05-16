#!/usr/bin/python3
"""
This module provides a script that fetches the status of the Holberton
School intranet using the urllib package.
"""
import urllib.request


def fetch_status():
    """
    Fetches the intranet status page and prints information about the response
    body, including its type, raw content, and UTF-8 decoded content.
    """
    url = "https://intranet.hbtn.io/status"
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
