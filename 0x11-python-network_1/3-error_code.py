#!/usr/bin/python3
"""
Module to send a request to a URL and display the body of the response.

This script sends an HTTP request to the specified URL and prints the body
of the response decoded in utf-8. If an HTTP error occurs, it prints the
error code.

Modules required:
    urllib.request: This module provides functions and classes to manage
    HTTP requests.
    urllib.error: This module provides error handling for HTTP requests.
    sys: This module provides access to some variables used or maintained
    by the interpreter.

Functions:
    main(argv): Sends a request to the URL and prints the response or error
    code.

Usage:
    Run the script from the command line with the URL as an argument.

Example:
    $ ./script_name.py http://example.com
"""

import urllib.request
import urllib.error
from sys import argv


def main(argv):
    """
    Sends a request to the passed URL and displays the body of the response.
    Manages urllib.error.HTTPError exceptions and prints the error code.

    Args:
        argv (list): A list of command line arguments including the script
        name and URL.
    """
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
            print(result.decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main(argv)
