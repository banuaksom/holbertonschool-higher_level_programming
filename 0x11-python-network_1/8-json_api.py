#!/usr/bin/python3
"""
takes a letter and sends POST request to http://0.0.0.0:5000/search_user
with letter as parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}

    req = requests.post("http://0.0.0.0:5000/search_user", data=data)
    if req.headers.get("content-type") != "application/json":
        print("Not a valid JSON")
    elif req.json() == {}:
        print("No result")
    else:
        print("[{}] {}".format(req.json()["id"], req.json()["name"]))
