#!/usr/bin/python3
"""
This module contains a script that sends a POST request to a given URL
with an email parameter, then prints the decoded body of the response.
"""
import sys
import urllib.parse
import urllib.request


def send_post_email():
    """
    Sends a POST request to the URL passed in sys.argv[1] containing the
    email passed in sys.argv[2], and displays the response body in UTF-8.
    """
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Pack data into a dictionary and encode it to URL format
    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    
    # Create the POST request object with data payload
    req = urllib.request.Request(url, data=encoded_data)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))


if __name__ == "__main__":
    send_post_email()
