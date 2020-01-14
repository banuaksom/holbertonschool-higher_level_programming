#!/usr/bin/python3
"""takes Github credentials and uses Github API to display id"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get("https://api.github.com/user",
                       auth=(argv[1], argv[2])).json()
    if "id" not in req:
        print("None")
    else:
        print(req.get("id"))
