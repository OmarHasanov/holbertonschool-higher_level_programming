#!/usr/bin/python3
"""
This module contains a script that sends a request to a specified URL and
displays the response body, safely handling any HTTP error exceptions.
"""
import sys
import urllib.error
import urllib.request


def fetch_url_safely():
    """
    Fetches the content of a URL from sys.argv[1]. Prints the UTF-8 decoded
    body on success, or catches HTTP errors and displays their status code.
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as error:
        # Utilizing .get() or direct attribute access for the code property
        print("Error code: {}".format(error.code))


if __name__ == "__main__":
    fetch_url_safely()
