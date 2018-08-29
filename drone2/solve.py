import pygame as pg, random, math
from pwn import *
from time import sleep

t = remote('127.0.0.1', 1338)

pg.init()

SCALE = 2

NMAP = [(1, 0), (0, 1), (-1, 0), (0, -1)]
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
size = width, height = 1000 * SCALE, 1000 * SCALE
current_pos = width // (2*SCALE), height // (2*SCALE)
current_direction = 0

display = pg.display
screen = display.set_mode(size)
clock = pg.time.Clock()

display.set_caption('Solve')

screen.fill(WHITE)
display.update()


def add_pos(pos, d):
    pos = list(pos)

    pos[0] += d[0]
    pos[1] += d[1]

    return tuple(pos)


ANGLE_DELTA = 2 * math.pi / 16

def block(pos):
    screen.fill(BLACK, ((SCALE*(pos[0]-1), SCALE*(pos[1]-1)), (SCALE*2+1, SCALE*2+1)))

def read_float():
    while True:
        x = None
        line = t.recvline().split()
        try:
            x = float(line[0])
        except:
            pass

        if x == None:
            print(' '.join(line))
        else:
            if len(line) > 1:
                print(' '.join(line[1:]))
            return x

def get_direction_vector(i, l):
    angle = {
        0: 0,
        1: math.pi / 2,
        2: math.pi,
        3: math.pi * 3 / 2,
    }[current_direction] + i * ANGLE_DELTA

    return (int(math.floor(math.cos(angle) * l)), int(math.floor(math.sin(angle) * l)))

def parse_pos():
    for i in xrange(16):
        collision = read_float()
        pos = add_pos(current_pos, get_direction_vector(i, collision))

        block(pos)


def tleft():
    global current_direction

    t.sendline('L')

    remove_drone()
    current_direction -= 1
    current_direction %= 4
    draw_drone()

    parse_pos()

def tright():
    global current_direction

    t.sendline('R')

    remove_drone()
    current_direction += 1
    current_direction %= 4
    draw_drone()

    parse_pos()

def tforward():
    global current_pos

    t.sendline('F')

    remove_drone()
    current_pos = add_pos(current_pos, NMAP[current_direction])
    draw_drone()

    parse_pos()

def tbackward():
    global current_pos

    t.sendline('B')

    remove_drone()
    current_pos = add_pos(current_pos, NMAP[(current_direction + 2) % 4])
    draw_drone()

    parse_pos()


def remove_drone():
    screen.fill(WHITE, ((SCALE*(current_pos[0]-2), SCALE*(current_pos[1]-2)), (SCALE*4+1, SCALE*4+1)))

def draw_drone():
    remove_drone()
    screen.fill(RED, ((SCALE*(current_pos[0]-2), SCALE*(current_pos[1]-2)), (SCALE*4+1, SCALE*4+1)))
    pos = add_pos(current_pos, get_direction_vector(0, 2))
    screen.fill(WHITE, ((SCALE*pos[0], SCALE*pos[1]), (1, 1)))



t.sendline('S')
parse_pos()
draw_drone()


key = None


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            key = event.key
        elif event.type == pg.KEYUP:
            key = None

    if key == pg.K_UP:
        tforward()
    elif key == pg.K_DOWN:
        tbackward()
    elif key == pg.K_LEFT:
        tleft()
        key = None
    elif key == pg.K_RIGHT:
        tright()
        key = None

    display.update()
    clock.tick(30)
