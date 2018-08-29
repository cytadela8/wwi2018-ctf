#!/usr/bin/python3

import binascii
import os
import sys

from Crypto.Cipher import AES
from Crypto import Random


with open(os.path.join(os.path.dirname(__file__), 'flag.txt')) as flag_file:
    flag = flag_file.read()

with open(os.path.join(os.path.dirname(__file__), 'key.txt'), 'rb') as key_file:
    key = key_file.read(16)

cipher = AES.new(key, AES.MODE_ECB)

with open(__file__) as code_file:
    sys.stdout.write(code_file.read())
    sys.stdout.flush()

while True:
    line = (sys.stdin.readline().strip() + flag).encode('utf-8')

    if not line:
        break

    while len(line) % 16 != 0:
        line += b'\0'

    sys.stdout.write(binascii.hexlify(cipher.encrypt(line)).decode('utf-8'))
    sys.stdout.write('\n')
    sys.stdout.flush()

