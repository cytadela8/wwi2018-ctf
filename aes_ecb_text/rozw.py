from pwn import *
import time


def getek(pocz):
    proc.write(pocz+"\n")
    return proc.readline().strip()


def split(data):
    assert len(data) % 32 == 0
    out = []
    for i in range(len(data)/32):
        out += [data[i*32: (i+1)*32]]
    return out

znaki = [chr(i) for i in range(32,128) if i!=ord(" ")]

flag_blocks = 4
flag_size = 16 * flag_blocks

ourflag = "." * flag_size
preflag = "." * flag_size

proc = remote("10.0.13.40", 1337)
#proc = process(["python3", "app.py"])

time.sleep(1)
proc.read()

test = split(getek(ourflag + preflag)[:flag_size*2*2])

assert len(test) == flag_blocks * 2
for el in test:
    assert el == test[0]

for i in range(flag_size-1, -1, -1):
    preflag = preflag[:-1]
    ourflag = ourflag[1:]
    found = False
    for znak in znaki:
        blocks = split(getek(ourflag + znak + preflag)[:flag_size*2*2])
        ourblocks = blocks[:flag_blocks]
        serverblocks = blocks[flag_blocks:flag_blocks*2]
        # print znak, ourblocks
        # print znak, serverblocks
        ok = True
        for i in range(flag_blocks):
            if ourblocks[i] != serverblocks[i]:
                ok = False
                break
        if ok:
            ourflag += znak
            found = True
            break
    if not found:
        print "It seems we are finished"
        break
    else:
        print ourflag

