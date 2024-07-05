#!/usr/bin/python3
"""
Module using request to fetche the link  https://intranet.hbtn.io/status
"""
import requests


def main():
    """
    Function that fetches https://intranet.hbtn.io/status
    """
    link = 'https://intranet.hbtn.io/status'
    r = requests.get(link)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))


if __name__ == "__main__":
    main()
