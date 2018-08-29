import numpy as np
from enum import Enum
from PIL import Image

class Field(Enum):
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    PINK = (255, 0, 255)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)

    @staticmethod
    def from_pixel(pixel):
        t = (pixel[0], pixel[1], pixel[2])
        return Field(t)

    def is_blocking(self):
        return self.name == "BLACK"

    def is_movable(self):
        return not self.is_blocked()

    def is_flag0(self):
        return self.name == "BLUE"

    def is_flag1(self):
        return self.name == "YELLOW"

    def is_flag2(self):
        return self.name == "GREEN"

    def is_misflag1(self):
        return self.name == "PINK"

    def is_misflag2(self):
        return self.name == "CYAN"

    def is_start(self):
        return self.name == "RED"


img = np.array(Image.open("map.png"))
MAP = list([[Field.from_pixel(pixel) for pixel in line] for line in img])

STARTING_POSES = []
y, x = 0, 0
for line in MAP:
    x = 0
    for field in line:
        assert(MAP[y][x] == field)
        if field.is_start():
            STARTING_POSES += [[x, y]]
        x += 1
    y += 1
