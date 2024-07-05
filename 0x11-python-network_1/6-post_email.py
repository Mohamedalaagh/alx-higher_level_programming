#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
"""
import requests
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
    link = argv[1]
    r = requests.post(link, data=values)
    print(r.text)


if __name__ == "__main__":
    main(argv)
