#!/usr/bin/python3
"""
Module to access the GitHub API and use the information.

This script takes GitHub credentials (username and password) as command
line arguments and uses the GitHub API to display the user's GitHub id.

Modules required:
    requests: This module allows you to send HTTP requests.
    requests.auth: This module provides authentication support.
    sys: This module provides access to some variables used or maintained
    by the interpreter.

Functions:
    main(argv): Takes GitHub credentials and prints the GitHub user id.

Usage:
    Run the script from the command line with your GitHub username and
    password as arguments.

Example:
    $ ./script_name.py <username> <password>
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Script that takes GitHub credentials (username and password) and uses
    the GitHub API to display the user's id.

    Args:
        argv (list): A list of command line arguments including the script
        name, GitHub username, and GitHub password.
    """
    user = argv[1]
    password = argv[2]
    response = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(user, password)
    )
    try:
        profile_info = response.json()
        print(profile_info['id'])
    except KeyError:
        print('None')


if __name__ == "__main__":
    main(argv)
