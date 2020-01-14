#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        status = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n"
              "\t- utf8 content: {}".format(
                  type(status), status, status.decode("utf-8")))
