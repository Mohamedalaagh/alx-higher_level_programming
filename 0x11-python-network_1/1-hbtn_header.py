#!/usr/bin/python3
"""
Script that fetches the value of the X-Request-Id variable from the header
of a response from a specified URL.

This script sends an HTTP GET request to a given URL and prints the value
of the X-Request-Id found in the response headers.

Modules required:
    urllib.request: This module provides functions and classes to manage
    HTTP requests.
    sys: This module provides access to some variables used or maintained
    by the interpreter.

Functions:
    main(argv): Sends a GET request to the URL and prints the X-Request-Id
    from the response headers.

Usage:
    Run the script from the command line with the URL as an argument.

Example:
    $ ./script_name.py http://example.com
"""

import urllib.request
from sys import argv


def main(argv):
    """
    Method that takes in a URL, sends a request to the URL, and displays
    the value of the X-Request-Id variable found in the header of the
    response.

    Args:
        argv (str): The URL to send the request to.
    """
    url = argv
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])


if __name__ == "__main__":
    main(argv[1])
