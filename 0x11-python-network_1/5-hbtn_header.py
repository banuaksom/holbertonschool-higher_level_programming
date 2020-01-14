#!/usr/bin/python3
"""takes URL, sends request to URL, displays value of X-Request-Id in header"""
from requests import get
from sys import argv


if __name__ == "__main__":
    print(get(argv[1]).headers.get("X-Request-Id"))
