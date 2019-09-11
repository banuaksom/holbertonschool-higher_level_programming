#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for i, l in enumerate(str):
        if i is n:
            s += ''
        else:
            s += l
    return s
