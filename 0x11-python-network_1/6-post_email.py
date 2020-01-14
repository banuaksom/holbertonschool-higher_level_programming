#!/usr/bin/python3
"""
takes a URL and email, sends POST request using parameters, displays body
of response
"""
import requests
from sys import argv


if __name__ == "__main__":
    print(requests.post(argv[1], data={"email": argv[2]}).text)
