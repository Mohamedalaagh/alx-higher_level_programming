#!/usr/bin/python3
"""
Module that sends a POST request to http://0.0.0.0:5000/search_user
with a specified letter as a parameter.
"""
import requests
from sys import argv


def main(argv):
    """
    Script that takes in a letter, sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter,
    and prints the result.

    Args:
        argv (list): A list of command line arguments including the script
        name and letter parameter.
    """
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)
    try:
        result = r.json()
        if bool(result) is False:
            print("No result")
        else:
            print("[{}] {}".format(result['id'], result['name']))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main(argv)
