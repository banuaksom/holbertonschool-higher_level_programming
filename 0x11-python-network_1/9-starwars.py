#!/usr/bin/python3
"""takes in a string and sends search request to Star Wars API"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get("https://swapi.co/api/people/?search={}".
                       format(argv[1])).json()
    print("Number of results:", req["count"])
    for val in req["results"]:
        print(val["name"])
