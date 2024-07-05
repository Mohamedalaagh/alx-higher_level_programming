#!/usr/bin/python3
"""
Module to send a POST request to a given URL with an email as a parameter.

This script sends an HTTP POST request to the specified URL with the given
email address as a parameter and displays the body of the response decoded
in utf-8.

Modules required:
    urllib.request: This module provides functions and classes to manage
    HTTP requests.
    sys: This module provides access to some variables used or maintained
    by the interpreter.

Functions:
    main(argv): Sends a POST request to the URL with the email and prints
    the response.

Usage:
    Run the script from the command line with the URL and email as
    arguments.

Example:
    $ ./script_name.py http://example.com test@example.com
"""

import urllib.request
import urllib.parse
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8).

    Args:
        argv (list): A list of command line arguments including the script
        name, URL, and email.
    """
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))


if __name__ == "__main__":
    main(argv)
