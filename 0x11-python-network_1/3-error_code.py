#!/usr/bin/python3
"""
takes URL, sends request to URL, displays body of response decoded in utf-8
"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
