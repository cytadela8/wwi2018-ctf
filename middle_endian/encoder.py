#!/usr/bin/python2

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def to_middle_endian(flag):
    lista = tobits(flag)
    out = ['x' for i in range(len(lista))]
    half = len(lista)//2
    for i in range(half):
        out[i] = lista[i*2]
    poz = 1
    for i in range(half):
        out[len(lista) -1 - i] = lista[i*2+1]
    return frombits(out)

def from_middle_endian(data):
    lista = tobits(data)
    out = ['x' for i in range(len(lista))]
    half = len(lista)//2
    for i in range(half):
        out[i*2] = lista[i]
    poz = 1
    for i in range(half):
        out[i*2+1] = lista[len(lista) -1 - i]
    return frombits(out)

import base64

flag = "CTF{7h1s_1S_MuR1cA}"
task = base64.b64encode(to_middle_endian(flag))
assert(from_middle_endian(base64.b64decode(task)) == flag)
print(task)


