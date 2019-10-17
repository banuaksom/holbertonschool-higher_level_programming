#!/usr/bin/python3
def number_of_lines(filename=""):
    num = 0
    with open(filename, encoding='utf8') as a_file:
        for line in a_file:
            num += 1
        return num
