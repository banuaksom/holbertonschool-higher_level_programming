#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    chars = ['.', '?', ':']
    s = ""
    line_pos = 0
    for i in text:
        if not (line_pos == 0 and i == ' '):
            s += i
            line_pos += 1
        if i in chars:
            s += '\n\n'
            line_pos = 0
    print(s, end='')
