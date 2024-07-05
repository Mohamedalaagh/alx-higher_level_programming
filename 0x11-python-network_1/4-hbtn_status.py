#!/usr/bin/python3
"""
Module to fetch the status from a specified URL using the requests module.

This script sends an HTTP GET request to the URL\
        https://intranet.hbtn.io/status
and prints the body of the response. The response details include the type
of the content and the content itself.

Modules required:
    requests: This module allows you to send HTTP requests.

Functions:
    main(): Fetches the status from the specified URL and prints the response.

Usage:
    Run the script directly from the command line to see the \
            output of the GET
    request.

Example:
    $ ./script_name.py
"""

import requests


def main():
    """
    Function that fetches https://intranet.hbtn.io/status.

    This function sends an HTTP GET request to the URL and prints:
    - The type of the response content.
    - The content of the response.
    """
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))


if __name__ == "__main__":
    main()
