#!/usr/bin/python3
for l in range(ord('z'), ord('a') - 1, -1):
    if l % 2 is 1:
        l -= ord(' ')
    print("{}".format(chr(l)), end="")
