import pyxel

from hexlib import *
from settings import *
from utils import *

def active_hex():
    return hex_round(pixel_to_hex(layout, Point(pyxel.mouse_x, pyxel.mouse_y)))
    
