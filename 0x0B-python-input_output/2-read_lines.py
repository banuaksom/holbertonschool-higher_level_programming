#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):

    with open(filename, encoding='utf8') as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end='')
        else:
            for line in range(nb_lines):
                print(a_file.readline(), end='')
