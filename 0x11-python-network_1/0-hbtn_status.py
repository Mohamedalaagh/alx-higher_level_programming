#!/usr/bin/python3
"""
Script that fetches the status of a specified URL.

This script sends an HTTP GET request to the URL \
        https://intranet.hbtn.io/status
and prints the body of the response. The response\
        details include the type of the
content, the raw content, and the UTF-8 decoded content.

Modules required:
    urllib.request: This module provides functions and classes to manage HTTP
    requests.

Functions:
    main(): Sends a GET request to the URL and prints\
            the details of the response.

Usage:
    Run the script directly from the command line to see the output of the GET
    request.

Example:
    $ ./script_name.py
"""
import urllib.request


def main():
    """
    Function to print the response of a specific URL.

    This function sends an HTTP GET request \
            to the URL https://intranet.hbtn.io/
    status. It then reads the response and prints:
    - The type of the response content.
    - The raw content of the response.
    - The UTF-8 decoded content of the response.
    """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))


if __name__ == "__main__":
    main()
