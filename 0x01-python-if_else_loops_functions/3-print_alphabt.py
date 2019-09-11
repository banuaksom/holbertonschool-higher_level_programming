#!/usr/bin/python3
for l in range(ord('a'), ord('z') + 1):
    if chr(l) not in ['e', 'q']:
        print("{}".format(chr(l)), end="")
