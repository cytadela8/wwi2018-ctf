#!/usr/bin/python3

import sys

with open(sys.argv[1]) as f:
    data = f.read()
    staty = {}
    for el in data:
        if el not in staty:
            staty[el] = 1
        else:
            staty[el] += 1
    for key, val in sorted(staty.items()):
        print (key, val)

