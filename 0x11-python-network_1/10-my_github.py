#!/usr/bin/python3
"""Login my github acount and authentique for get data."""
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        'https://api.github.com/user', auth=(username, password))
    data = response.json()
    print(data.get('id'))
