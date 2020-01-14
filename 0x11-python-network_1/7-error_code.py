#!/usr/bin/python3
"""Takes URL, sends request to URL, displays body of response"""
import requests
from sys import argv


if __name__ == "__main__":
    status = requests.get(argv[1]).status_code
    if status >= 400:
        print("Error code:", status)
    else:
        print(requests.get(argv[1]).text)
