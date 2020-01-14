#!/usr/bin/python3
"""takes in URL, sends request, displays value of X-Request-Id from header"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.info().get("X-Request-Id"))
