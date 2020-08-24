#!/usr/bin/python3
"""Script that fetches to url and get X-Request-Id."""
import requests
import sys

if __name__ == '__main__':
    dato = sys.argv[1] if len(sys.argv) == 2 else ""
    params = {'q': dato}
    response = requests.post('http://0.0.0.0:80/search_user', data=params)
    if len(response.json()) != 0:
        data = response.json()
        if data is not dict:
            print("Not a valid JSON")
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")