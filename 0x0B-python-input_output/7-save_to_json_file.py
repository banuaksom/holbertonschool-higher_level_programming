#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf8') as a_file:
        return a_file.write(json.dumps(my_obj))
