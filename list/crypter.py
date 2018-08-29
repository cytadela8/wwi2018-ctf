#!/usr/bin/python3

import random
import string

alfabetstring = string.ascii_lowercase + "ąęźćłóżń"


konwersjalista = list(alfabetstring)
random.shuffle(konwersjalista)
konwersjalistabig = [x.upper() for x in konwersjalista]

konwersjalista += konwersjalistabig
alfabetstring += alfabetstring.upper()

print ("".join(konwersjalista))

konwersja = {}

for i in range(len(alfabetstring)):
    konwersja[alfabetstring[i]] = konwersjalista[i]

print(konwersja)

import sys

with open(sys.argv[1]) as f:
    clear = f.read()
    with open("list.out", "w") as fout:
        for c in clear:
            if c not in konwersja:
                fout.write(c)
            else:
                fout.write(konwersja[c])





