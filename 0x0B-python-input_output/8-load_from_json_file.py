#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, encoding='utf8') as a_file:
        return json.load(a_file)
