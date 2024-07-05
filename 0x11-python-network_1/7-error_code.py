#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response
or handles HTTP errors.

Modules required:
    requests: This module allows you to send HTTP requests.
    sys: This module provides access to some variables used or maintained
    by the interpreter.

Functions:
    main(argv): Sends a request to the URL and prints the response or
    handles HTTP errors.

Usage:
    Run the script from the command line with the URL as an argument.

Example:
    $ ./script_name.py http://example.com
"""

import requests
from sys import argv


def main(argv):
    """
    Method that manages HTTP errors and prints the body of the response
    or an error code.

    Args:
        argv (list): A list of command line arguments including the script
        name and URL.
    """
    url = argv[1]
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))


if __name__ == "__main__":
    main(argv)
