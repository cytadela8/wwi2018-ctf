import random
import socket
import math
import traceback
from threading import Thread
from os import environ

from parse_map import STARTING_POSES, MAP

TCP_PORT = int(environ.get('PORT', '9000'))
TCP_HOST = environ.get('HOST', '127.0.0.1')
NMAP = [(1, 0), (0, 1), (-1, 0), (0, -1)]
FLAG0 = b'#flag CTF{v3rY_F1r5T_ST3ps}\n'
FLAG1 = b'#flag CTF{K33p_601n6_fUr7h3r}\n'
FLAG2 = b'#flag CTF{1s_Th1S_th3_f1N4l_R00m?}\n'
MISFLAG = b'NOT THIS WAY!\n'
BUFFER_SIZE = 20
MAX_CONNECTIONS = 1000
TIMEOUT = 60
SCAN_DENSITY = 16
DELTA_STEP = 0.02
COLLISION_RANGE = 1
DEBUG = False


class Destroyed(Exception):
    pass


def get_map_field(pos):
    return MAP[pos[1]][pos[0]]


def get_ray(pos, angle):
    pos = list(pos)

    delta = [math.cos(angle), math.sin(angle)]
    delta[0] *= DELTA_STEP
    delta[1] *= DELTA_STEP
    dist = 0

    while True:
        if get_map_field((math.floor(pos[0]), math.floor(pos[1]))).is_blocking():
            return dist
        else:
            pos[0] += delta[0]
            pos[1] += delta[1]
            dist += DELTA_STEP


ANGLE_DELTA = 2 * math.pi / SCAN_DENSITY

def get_all_rays(pos, direction):
    angle = {
        0: 0,
        1: math.pi / 2,
        2: math.pi,
        3: math.pi * 3 / 2,
    }[direction]

# TODO: print flags

    rays = []

    for i in range(SCAN_DENSITY):
        rays.append(get_ray(pos, angle))
        angle += ANGLE_DELTA

    return rays


def move_pos(pos, direction, v):
    pos = list(pos)

    direction %= 4

    pos[0] += v * NMAP[direction][0]
    pos[1] += v * NMAP[direction][1]

    for y in range(-COLLISION_RANGE, COLLISION_RANGE+1):
        for x in range(-COLLISION_RANGE+abs(y), COLLISION_RANGE-abs(y)+1):
            if get_map_field((pos[0] + x, pos[1] + y)).is_blocking():
                raise Destroyed("Destroyed")

    return pos


class ThreadedConnection(Thread):
    def __init__(self, client, address):
        Thread.__init__(self)
        self.client = client
        self.address = address
        self.started = False
        self.pos = list(random.choice(STARTING_POSES))
        self.direction = random.randrange(5)
        self.got_flag0 = False
        self.got_flag1 = False
        self.got_flag2 = False
        self.got_misflag1 = False
        self.got_misflag2 = False
        self.destroyed = False

    def run(self):
        if DEBUG:
            print(f"New connection from address {self.address}.")

        while True:
            try:
                if self.destroyed:
                    try:
                      self.client.recv(BUFFER_SIZE)
                      self.client.close()
                    except:
                      pass
                    return
                else:
                    data = self.client.recv(1)
                if DEBUG:
                    print("data received:", data)
                if data:
                    for c in data:
                        self.handle(chr(c))
                else:
                    self.client.close()
                    raise Exception("Connection closed")
            except:
                try:
                    self.client.close()
                except:
                    pass

                if DEBUG:
                    print("Error, closing connection.")
                    traceback.print_exc()

                return

    def handle(self, c):
        if self.destroyed:
            return

        print("handle:", c)
        {
            'S': self.init_drone,
            'L': self.left,
            'R': self.right,
            'F': self.forward,
            'B': self.backward,
            '\r': lambda: None,
            '\n': lambda: None,
            ' ':  lambda: None,
            '\t': lambda: None,
        }.get(c, self.unrecognized)()

    def init_drone(self):
        if self.started:
            self.unrecognized()
            return

        if DEBUG:
            print("starting_pos:", f"({self.pos[0]}, {self.pos[1]})")

        self.started = True
        self.print_pos()

    def left(self):
        self.rotate(-1)

    def right(self):
        self.rotate(1)

    def forward(self):
        self.move(1)

    def backward(self):
        self.move(-1)

    def unrecognized(self):
        self.client.sendall(b"Unrecognized command!\n")

        try:
            self.client.shutdown();
            self.client.close()
        except:
            pass

        if DEBUG:
            print("Connection closed.")

    def rotate(self, d):
        if not self.started:
            self.unrecognized()
            return

        self.direction += d
        self.direction %= 4
        self.print_pos()


    def move(self, v):
        if not self.started:
            self.unrecognized()
            return

        try:
            self.pos = move_pos(self.pos, self.direction, v)
            self.print_pos()
        except Destroyed:
            self.destroyed = True
            print("Destroyed.")

    def print_pos(self):
        response = ""
        #  response += f"{self.pos[0]} {self.pos[1]}\n"

        field = get_map_field(self.pos)
        if not self.got_flag0 and field.is_flag0():
            self.got_flag0 = True
            self.print_flag0()
        if not self.got_flag1 and field.is_flag1():
            self.got_flag1 = True
            self.print_flag1()
        if not self.got_flag2 and field.is_flag2():
            self.got_flag2 = True
            self.print_flag2()
        if not self.got_misflag1 and field.is_misflag1():
            self.got_misflag1 = True
            self.print_misflag()
        if not self.got_misflag2 and field.is_misflag2():
            self.got_misflag2 = True
            self.print_misflag()

        if DEBUG:
            print(field)

        collisions = get_all_rays(self.pos, self.direction)
        for dist in collisions:
            response += f"{dist}\n"

        self.client.sendall(response.encode())

    def print_flag0(self):
        self.client.sendall(FLAG0)

    def print_flag1(self):
        self.client.sendall(FLAG1)

    def print_flag2(self):
        self.client.sendall(FLAG2)

    def print_misflag(self):
        self.client.sendall(MISFLAG)



class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(MAX_CONNECTIONS)
        print(f"Listening... host: {self.host}, port: {self.port}")
        while True:
            client, address = self.sock.accept()
            client.settimeout(TIMEOUT)
            conn = ThreadedConnection(client, address)
            conn.start()



ThreadedServer(TCP_HOST, TCP_PORT).listen()
